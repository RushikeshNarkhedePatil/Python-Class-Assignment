# 2. Write a program which accepts one number and prints sum of rst N natural numbers.
# Input: 5
# Output: 15

def PrintNaturalNumber(no):
    iSum = 0
    for i in range(1,no+1):
        iSum =iSum +i
    return iSum



def main():
    Number = int(input("Enter Number : "))

    Sum = PrintNaturalNumber(Number)
    print("Summention of natural number is : ",Sum)

if __name__ == "__main__":
    main()