# 10: Design a Python application that creates two threads.
# •Thread 1 should compute the sum of elements from a list.
# •Thread 2 should compute the product of elements from the same list.
# •Return the results to the main thread and display them.

import threading
import time

def SumOfElements(numbers):
    total_sum = sum(numbers)
    print("Sum of elements is : ", total_sum)
    print("Thread ID : ", threading.get_ident())
    print("Thread Name : ", threading.current_thread().name)

def ProductOfElements(numbers):
    product = 1
    for num in numbers:
        product = product * num
    print("Product of elements is : ", product)
    print("Thread ID : ", threading.get_ident())
    print("Thread Name : ", threading.current_thread().name)

def main():
    data = [1, 2, 3, 4, 5]
    SumThread = threading.Thread(target=SumOfElements, args=(data,))
    ProductThread = threading.Thread(target=ProductOfElements, args=(data,))

    start_time = time.time()
    SumThread.start()
    ProductThread.start()

    SumThread.join()
    ProductThread.join()

    end_time = time.time()

    print("Total Execution time :", end_time - start_time)
    print("End of main thread")

if __name__ == "__main__":
    main()