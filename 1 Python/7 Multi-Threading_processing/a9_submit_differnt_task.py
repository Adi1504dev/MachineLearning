from concurrent.futures import ThreadPoolExecutor

def task1(x):
    return f"Task1: {x * 3}"

def task2(x, y):
    return f"Task2: {x + y}"

with ThreadPoolExecutor() as ex:
    futures = []
    futures.append(ex.submit(task1, 5))
    futures.append(ex.submit(task2, 3, 7))

    for f in futures:
        print(f.result())