# 1: Design a Python application that creates two threads named Prime and NonPrime.
# •Both threads should accept a list of integers.
# •The Prime thread should display all prime numbers from the list.
# •The NonPrime thread should display all non-prime numbers from the list.

import threading
import time

def Prime(numbers):
    print("Prime Numbers are:")
    for num in numbers:
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                print(num)
    print("Thread ID : ", threading.get_ident())
    print("Thread Name : ", threading.current_thread().name)

def NonPrime(numbers):
    print("Non-Prime Numbers are:")
    for num in numbers:
        if num <= 1:
            print(num)
        else:
            for i in range(2, int(num**0.5) + 1):
                if (num % i) == 0:
                    print(num)
                    break
    print("Thread ID : ", threading.get_ident())
    print("Thread Name : ", threading.current_thread().name)

def main():
    data = [10, 15, 23, 42, 7, 3, 4, 5, 16, 19, 20, 1, 0, -5]
    PrimeThread = threading.Thread(target=Prime, args=(data,))
    NonPrimeThread = threading.Thread(target=NonPrime, args=(data,))

    start_time = time.time()
    PrimeThread.start()
    NonPrimeThread.start()

    PrimeThread.join()
    NonPrimeThread.join()

    end_time = time.time()

    print("Total Execution time :", end_time - start_time)
    print("End of main thread")

if __name__ == "__main__":
    main()