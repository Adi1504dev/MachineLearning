import random
from concurrent.futures import ThreadPoolExecutor, as_completed

def risky_task(n):
    if random.random() < 0.5:
        raise Exception(f"Failed task {n}")
    return f"Completed task {n}"

with ThreadPoolExecutor(max_workers=3) as ex:
    futures = {ex.submit(risky_task, i): i for i in range(5)}

    for f in as_completed(futures):
        task_id = futures[f]
        try:
            result = f.result()
            print(result)
        except Exception as e:
            print(f"Retrying task {task_id}...")
            retry_f = ex.submit(risky_task, task_id)
            try:
                print(retry_f.result())
            except Exception as e:
                print(f"Task {task_id} failed again.")