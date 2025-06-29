"""
🧵 Multithreading
Runs multiple threads (lightweight subprocesses) within a single process.

Threads share memory.

In CPython, threads are limited by the GIL (Global Interpreter Lock) — only one thread executes Python bytecode at a time.

Best for I/O-bound tasks (e.g., web scraping, file reading, network calls).

✅ Example Use Cases:
Reading multiple files simultaneously.

Making many API calls in parallel.


🔥 Multiprocessing
Runs multiple processes, each with its own memory space.

Bypasses the GIL, so it uses multiple CPU cores effectively.

Best for CPU-bound tasks (e.g., image processing, model training).

✅ Example Use Cases:
Data transformation on large datasets.

Parallel mathematical computations.




⚡ Can You Combine Both?
Yes! You can combine multithreading and multiprocessing to leverage both:

Use multiprocessing to fully utilize multiple CPU cores.

Inside each process, you can use multithreading for concurrent I/O tasks.

🔧 Example Use Case:
Multiprocessing to run jobs on separate CPU cores.

Within each process, use threads to download multiple files in parallel.


"""


from multiprocessing import Process
from threading import Thread
import time

def download_files(process_name):
    def download(file):
        time.sleep(2)
        print(f"Process {process_name}: Downloading {file}")

    threads = []
    for i in range(5):
        t = Thread(target=download, args=(f"file_{i}",))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == "__main__":
    p1 = Process(target=download_files, args=("A",))
    p2 = Process(target=download_files, args=("B",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()