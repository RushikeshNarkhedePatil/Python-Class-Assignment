# 3: Design a Python application where multiple threads update a shared variable.
# •Use a Lock to avoid race conditions.
# •Each thread should increment the shared counter multiple times.
# •Display the nal value of the counter after all threads complete execution.

import threading
import time

shared_counter = 0
lock = threading.Lock()

def increment_counter(num_increments):
    global shared_counter
    for _ in range(num_increments):
        with lock:
            shared_counter = shared_counter + 1
    print("Thread ID : ", threading.get_ident())
    print("Thread Name : ", threading.current_thread().name)

def main():
    num_threads = 5
    increments_per_thread = 100000

    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=increment_counter, args=(increments_per_thread,))
        threads.append(thread)

    start_time = time.time()
    
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()

    print("Final value of shared counter :", shared_counter)
    print("Total Execution time :", end_time - start_time)
    print("End of main thread")

if __name__ == "__main__":
    main()