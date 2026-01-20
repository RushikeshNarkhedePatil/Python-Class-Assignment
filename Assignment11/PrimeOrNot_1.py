# 1. Write a program which accepts one number and checks whether it is prime or not.
# Input: 11
# Output: Prime Number

def PrimeOrNot(no):
    Status  = False

    if(no == 2):
        return True

    for i in range(2,no+1):
        if(i %2 != 0):
            Status = True
        else:
            Status = False

    return Status

def main():
    Number = int(input("Enter Number to print table : "))

    Status = PrimeOrNot(Number)
    if(Status):
        print("Prime Numer")
    else:
        print("Not Prime")

if __name__ == "__main__":
    main()