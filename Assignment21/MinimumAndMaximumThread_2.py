# 2: Design a Python application that creates two threads.
# •Thread 1 should calculate and display the maximum element from an list.
# •Thread 2 should calculate and display the minimum element from the same list.
# •The list should be accepted from the user.

import threading
import time

def Maximum(numbers):
    max_value = max(numbers)
    print("Maximum value is : ", max_value)
    print("Thread ID : ", threading.get_ident())
    print("Thread Name : ", threading.current_thread().name)

def Minimum(numbers):
    min_value = min(numbers)
    print("Minimum value is : ", min_value)
    print("Thread ID : ", threading.get_ident())
    print("Thread Name : ", threading.current_thread().name)

def main():
    #accept user input list
    print("Enter numbers separated by space:")
    # Uncomment the following line to accept user input
    data = list(map(int, input().split()))
    # For demonstration purposes, using a predefined list
    #data = [34, 12, 5, 67, 23, 89, 1, 45, 78, 3]
    MaxThread = threading.Thread(target=Maximum, args=(data,))
    MinThread = threading.Thread(target=Minimum, args=(data,))

    start_time = time.time()
    MaxThread.start()
    MinThread.start()

    MaxThread.join()
    MinThread.join()

    end_time = time.time()

    print("Total Execution time :", end_time - start_time)
    print("End of main thread")

if __name__ == "__main__":
    main()
