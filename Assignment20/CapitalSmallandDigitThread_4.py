# 4: Design a Python application that creates three threads named Small, Capital, and
# Digits.
# •All threads should accept a string as input.
# •The Small thread should count and display the number of lowercase characters.
# •The Capital thread should count and display the number of uppercase characters.
# •The Digits thread should count and display the number of numeric digits.
# •Each thread must also display:
# ◦Thread ID
# ◦Thread Name

import threading
import time

def Captital(Value):
    icnt =0
    for char in Value:
        if(char >='A' and char <= 'Z'):
            icnt = icnt + 1
    print("Count of Capital is : ", icnt)
    print("Thread ID : ", threading.get_ident())
    print("Thread Name : ", threading.current_thread().name)

def Small(Value):
    icnt =0
    for i in range(len(Value)):
        if(Value[i] >='a' and Value[i] <= 'z'):
            icnt = icnt + 1
    print("Count of Small is : ", icnt)
    print("Thread ID : ", threading.get_ident())
    print("Thread Name : ", threading.current_thread().name)

def Digit(Value):
    icnt = 0
    for i in range(len(Value)):
        if(Value[i] >='0' and Value[i] <= '9'):
            icnt = icnt + 1

    print("Count of Digit is : ", icnt)
    print("Thread ID : ", threading.get_ident())
    print("Thread Name : ", threading.current_thread().name)

def main():
    data = "abcABCdefDEFghiGHI96jklJKL37mnoMNO72pqrPQR75stuSTU48vwxyzVWXYZ"
    CapitalThread = threading.Thread(target=Captital,args=(data,))
    SmallThread = threading.Thread(target=Small, args=(data,))
    DigitThread = threading.Thread(target=Digit,args=(data,))

    start_time = time.time()
    CapitalThread.start()
    SmallThread.start()
    DigitThread.start()

    CapitalThread.join()
    SmallThread.join()
    DigitThread.join()

    end_time = time.time()

    print("Total Execution time :",end_time - start_time)
    print("End of main thread")

if __name__ == "__main__":
    main()