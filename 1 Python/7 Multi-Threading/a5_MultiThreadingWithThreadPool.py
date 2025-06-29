from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime
import time

def print_number(number):
    time.sleep(2)
    return f"Number = {number}"

numbers=[1,2,3,4,5,6,7,8,9,10]

time1=datetime.now()
with ThreadPoolExecutor(max_workers=4) as ex:
    results=ex.map(print_number,numbers)


for result in results:
    print(result)
print(f"finish {datetime.now()-time1}")

