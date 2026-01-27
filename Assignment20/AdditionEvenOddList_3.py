# 3: Design a Python application that creates two threads named EvenList and OddList.
# •Both threads should accept a list of integers as input.
# •The EvenList thread should:
# • Extract all even elements from the list.
# ◦Calculate and display their sum.
# The OddList thread should:
# ◦Extract all odd elements from the list.
# ◦Calculate and display their sum.
# Threads should run concurrently.

import threading
import time

def EvenSum(Numbers):
    sum =0
    for i in range(len(Numbers)):
        if(Numbers[i] % 2 == 0):
            sum = sum + Numbers[i]
    print("Sum of even list numbers : ",sum)


def OddSum(Numbers):
    sum =0
    for i in range(len(Numbers)):
        if(Numbers[i] % 2 != 0):
            sum = sum + Numbers[i]

    print("Sum of odd list  numbers : ",sum)


def main():
    numbers = [11,21,22,14,55,77,66,99,13,17,82,45]
    start_time = time.time()
    t1 = threading.Thread(target=EvenSum,args=(numbers,))
    t2 = threading.Thread(target=OddSum,args=(numbers,))
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    end_time = time.time()

    print("Total Execution time is : ",end_time-start_time)
    print("End of Main thread")

if __name__ =="__main__":
    main()

