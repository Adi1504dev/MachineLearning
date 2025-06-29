"""
f.running()      # True if currently running
f.done()         # True if completed
f.cancelled()    # True if cancelled before starting
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def task(n):
    time.sleep(2)
    return f"Task {n} done"

with ThreadPoolExecutor(max_workers=3) as ex:
    ## creates dictionary of future and number
    futures = {ex.submit(task, i): i for i in range(5)}
    """for f in futures:
        means you're looping over the keys of the dictionary → and those keys are Future objects.  """
    # Periodically check which tasks are still running
    while True:
        still_running = [futures[f] for f in futures if f.running() and not f.done()]
        if still_running:
            print(f"Still running: {still_running}")
            time.sleep(1)  # Wait a bit before checking again
        else:
            break

    # Print final results
    for f in as_completed(futures):
        print(f.result())