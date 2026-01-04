from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime
import time

def print_number(number):
    time.sleep(2)
    return f"Number = {number}"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

time1 = datetime.now()
if __name__=="__main__":
    with ProcessPoolExecutor(max_workers=4) as ex:
        futures = ex.map(print_number, numbers) #here we use map so it returns a generator and we give list of numbers
        #It is generator so even if task at poition 10 is completed first it will wait for previous tasks to complete
    print(type(futures)) # <class 'generator'> Calculated Value
    for result in futures:
        print(result)
    print(f"Finished in {datetime.now() - time1}")
