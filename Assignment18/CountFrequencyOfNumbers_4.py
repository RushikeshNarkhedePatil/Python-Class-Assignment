# 4.Write a program which accept N numbers from user and store it into List. Accept one another
# number from user and return frequency of that number from List.
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 5 34 2 5 65
# Element to search : 5
# Output : 3

def CountFrequencyOfNumber(numbers,findnumber):
    icnt = 0
    for no in numbers:
        if(no == findnumber):
            icnt = icnt + 1

    return icnt


def main():
    Numbers = []
    no = int(input("Enter number of count to add on list : "))

    for i in range(no):
        No = int(input())
        Numbers.append(No)

    find = int(input("Enter Number to Find Frequency : "))
    Result = CountFrequencyOfNumber(Numbers,find)
    print(f"Frequency {find} is  : ",Result)

if __name__ == "__main__":
    main()