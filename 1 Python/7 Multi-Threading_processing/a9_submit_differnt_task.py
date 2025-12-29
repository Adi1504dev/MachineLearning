from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep

def task1(x):
    sleep(2)
    return f"Task1: {x * 3}"

def task2(x, y):
    return f"Task2: {x + y}"

with ThreadPoolExecutor() as ex:
    futures = []
    futures.append(ex.submit(task1, 5))
    futures.append(ex.submit(task2, 3, 7))

    for f in as_completed(futures):
        print(f.result())