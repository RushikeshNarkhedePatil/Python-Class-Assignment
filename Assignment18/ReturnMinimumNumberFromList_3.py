# 3.Write a program which accept N numbers from user and store it into List. Return Minimum
# number from that List.
# Input : Number of elements : 4
# Input Elements : 13 5 45 7
# Output : 5

def MaximumOfNumber(numbers):
    Min = numbers[0]
    for no in numbers:
        if(no < Min):
            Min = no
    return Min

def main():
    Numbers = []
    no = int(input("Enter number of count to add on list : "))

    for i in range(no):
        No = int(input())
        Numbers.append(No)

    Result = MaximumOfNumber(Numbers)
    print("Minimum of N Numbers is : ",Result)

if __name__ == "__main__":
    main()