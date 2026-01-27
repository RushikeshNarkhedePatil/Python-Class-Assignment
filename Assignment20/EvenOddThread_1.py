import threading

def Even():
    for i in range(1,21):
        if(i % 2 == 0):
            print("Even Number is : ",i)

def Odd():
    for i in range(1,21):
        if(i % 2 != 0):
            print("Odd Number is : ",i)



def main():
    t1 = threading.Thread(target=Even)
    t1.start()

    t2 = threading.Thread(target=Odd)
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()

