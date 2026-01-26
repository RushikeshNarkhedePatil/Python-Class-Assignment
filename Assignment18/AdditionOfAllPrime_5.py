# 5.Write a program which accept N numbers from user and store it into List. Return addition of all
# prime numbers from that List. Main python file accepts N numbers from user and pass each
# number to ChkPrime() function which is part of our user defined module named as
# MarvellousNum. Name of the function from main python file should be ListPrime().

# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 10 34 2 5 8
# Output : 54 (13 + 5 + 7 +2 + 5)

from MarvellousNum import CheckPrime

def ListPrime(numbers):
    sum = 0
    for no in numbers:
        if(CheckPrime(no) == True):
            sum = sum + no
    return sum

def main():
    Numbers = []
    no = int(input("Enter number of count to add on list : "))

    for i in range(no):
        No = int(input())
        Numbers.append(No)

    Result = ListPrime(Numbers)
    print("Addition of All Prime Numbers is : ",Result)

if __name__ == "__main__":
    main()