import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def risky_task(task_id):
    """A sample task that fails on ID 3 to demonstrate retries."""
    if task_id == 3:
        raise ValueError("Simulated connection error")
    return f"Data for task {task_id}"

# 1. Define the maximum attempts allowed
MAX_ATTEMPTS = 3

with ThreadPoolExecutor(max_workers=3) as ex:
    # 2. Map the Future object to a tuple: (the actual ID, which attempt this is)
    # Start all tasks as 'Attempt 1'
    futures = {ex.submit(risky_task, i): (i, 1) for i in range(5)}

    # 3. Use a while loop because the 'futures' dict will change as we add retries
    while futures:
        # as_completed returns tasks the moment they finish (success or failure)
        # We wrap in list() to avoid "dictionary changed size during iteration" errors
        for f in as_completed(list(futures.keys())):
            
            # Remove the finished task from our tracking dictionary
            task_id, attempt = futures.pop(f)
            
            try:
                # 4. Try to get the result
                result = f.result()
                print(f"✅ Task {task_id}: Success on attempt {attempt}")
            
            except Exception as e:
                # 5. If it fails, check if we have retries left
                if attempt < MAX_ATTEMPTS:
                    print(f"⚠️ Task {task_id}: Failed (Attempt {attempt}). Retrying...")
                    
                    # OPTIONAL: Wait a moment before retrying (prevents spamming a failing server)
                    time.sleep(0.5) 
                    
                    # 6. RE-SUBMIT: Start the task again and increment the attempt counter
                    new_f = ex.submit(risky_task, task_id)
                    futures[new_f] = (task_id, attempt + 1)
                else:
                    # 7. FINAL FAILURE: We hit the limit
                    print(f"❌ Task {task_id}: FAILED permanently after {attempt} attempts.")

            # 8. CRITICAL: Break the 'as_completed' loop and restart the 'while' loop.
            # This ensures 'as_completed' sees the new 'new_f' we just added.
            break