# 5.Write a program which accepts one number and prints all odd numbers till that number.
def PrintOdd(no):
    for i in range(1,no+1):
        if(i %2 !=0):
            print(i,end=" ")
    print()

def main():
    Number = int(input("Enter Number to print table : "))

    PrintOdd(Number)

if __name__ == "__main__":
    main()