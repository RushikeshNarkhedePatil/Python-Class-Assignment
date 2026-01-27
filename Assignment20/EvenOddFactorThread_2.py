# 2: Design a Python application that creates two threads named EvenFactor and
# OddFactor.
# •Both threads should accept one integer number as a parameter.
# •The EvenFactor thread should:
# •
# •
# ◦Identify all even factors of the given number.
# ◦Calculate and display the sum of even factors.
# The OddFactor thread should:
# ◦Identify all odd factors of the given number.
# ◦Calculate and display the sum of odd factors.
# After both threads complete execution, the main thread should display the message:
# “Exit from main”

import threading
import time

def EvenFactor(No1):
    sum =0
    for i in range(1,No1+1):
        if(No1 % i == 0):
            if(i%2==0):
                sum = sum + i
    print("Sum of even Factor : ",sum)


def OddFactor(No1):
    sum =0
    for i in range(1,No1+1):
        if(No1 % i == 0):
            if(i%2!=0):
                sum = sum + i

    print("Sum of odd Factor : ",sum)


def main():
    start_time = time.time()
    t1 = threading.Thread(target=EvenFactor,args=(10000000,))
    t1.start()
    t2 = threading.Thread(target=OddFactor,args=(10000000,))
    t2.start()

    t1.join()
    t2.join()
    end_time = time.time()

    print("Total Execution time is : ",end_time-start_time)

if __name__ =="__main__":
    main()

