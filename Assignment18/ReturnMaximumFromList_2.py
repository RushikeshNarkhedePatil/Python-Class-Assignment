# 2.Write a program which accept N numbers from user and store it into List. Return Maximum
# number from that List.

def MaximumOfNumber(numbers):
    Max = 0
    for no in numbers:
        if(no > Max):
            Max = no
    return Max

def main():
    Numbers = []
    no = int(input("Enter number of count to add on list : "))

    for i in range(no):
        No = int(input())
        Numbers.append(No)

    Result = MaximumOfNumber(Numbers)
    print("Maximum of N Numbers is : ",Result)

if __name__ == "__main__":
    main()