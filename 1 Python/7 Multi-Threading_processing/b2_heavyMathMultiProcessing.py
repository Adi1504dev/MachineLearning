from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime
import math
import sys
import time

def num_fact(number):
    return f"Factorial of {number} = {math.factorial(number)}"

# To Get result else python would feel like someone hacking and will fail
sys.set_int_max_str_digits(1000000000)

numbers = [5000,40000,2000,433,4223,32345,3223,54353,23234,23432,3,2312,3443,234,32,42,1232,432,4,23,423,4234,234,23,4,234,23,4,32442,34,234]

time1 = datetime.now()
if __name__=="__main__":
    with ProcessPoolExecutor(max_workers=1) as ex: # Change workers to see differance in runtime 03.881174 sec in 1 , 1.73 sec in 3
        futures = [ex.submit(num_fact,num) for num in numbers]
    for f in as_completed(futures):
        print(f.result())
    print(f"Finished in {datetime.now() - time1}")
