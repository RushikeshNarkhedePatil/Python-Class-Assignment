# 1.Write a program which accept N numbers from user and store it into List. Return addition of all
# elements from that List.
# Input : Number of elements : 6
# Input Elements : 13 5 45 7 4 56
# Output : 130

def AdditionOfNElements(numbers):
    sum = 0
    for no in numbers:
        sum = sum + no
    return sum

def main():
    Numbers = []
    no = int(input("Enter number of count to add on list : "))

    for i in range(no):
        No = int(input())
        Numbers.append(No)

    Result = AdditionOfNElements(Numbers)
    print("Addition of N Numbers is : ",Result)

if __name__ == "__main__":
    main()

