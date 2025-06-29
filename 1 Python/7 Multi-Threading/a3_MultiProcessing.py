import multiprocessing
import time

# Task 1: Square numbers
def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i * i}")

# Task 2: Cube numbers using kwargs
def cube_numbers(*n):
    for i in range(n[0]):
        time.sleep(1.5)
        print(f"Cube: {i * i * i}")

if __name__ == "__main__":
    # Start timing
    t = time.time()

    # Create processes
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers, args=(4,6))

    # Start processes
    p1.start()
    p2.start()

    # Wait for both processes to complete
    p1.join()
    p2.join()

    # Total time taken
    finished_time = time.time() - t
    print(f"Finished time: {finished_time:.2f} seconds")
