from concurrent.futures import ThreadPoolExecutor

def add(x, y): return f"add: {x + y}"
def mul(x, y): return f"mul: {x * y}"

def dispatcher(task):
    func, x, y = task
    return func(x, y)

tasks = [
    (add, 2, 3),
    (mul, 4, 5),
    (add, 7, 1),
    (mul, 3, 3),
]

with ThreadPoolExecutor() as ex:
    results = ex.map(dispatcher, tasks)

for r in results:
    print(r)