# 5: Design a Python application that creates two threads named Thread1 and Thread2.
# •Thread1 should display numbers from 1 to 50.
# •Thread2 should display numbers from 50 to 1 in reverse order.
# •Ensure that:
# ◦
# Use appropriate thread synchronizatio
# •Thread2 starts execution only after Thread1 has completed.

import threading
import time

def DisplayAscending():
    for i in range(1, 51):
        print("Thread1 - Ascending:", i)
        time.sleep(0.1)
    print("Thread1 Completed")
    print("Thread ID : ", threading.get_ident())
    print("Thread Name : ", threading.current_thread().name)
    
def DisplayDescending():
    for i in range(50, 0, -1):
        print("Thread2 - Descending:", i)
        time.sleep(0.1)
    print("Thread2 Completed")
    print("Thread ID : ", threading.get_ident())
    print("Thread Name : ", threading.current_thread().name)

def main():
    AscendingThread = threading.Thread(target=DisplayAscending)
    DescendingThread = threading.Thread(target=DisplayDescending)

    start_time = time.time()
    
    AscendingThread.start()
    AscendingThread.join()  # Ensure Thread2 starts only after Thread1 completes

    DescendingThread.start()
    DescendingThread.join()

    end_time = time.time()

    print("Total Execution time :", end_time - start_time)
    print("End of main thread")

if __name__ == "__main__":
    main()