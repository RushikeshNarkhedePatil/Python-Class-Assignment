# 3. Write a program which accepts one number and prints sum of digits.
# Input: 123
# Output: 6

def SumOfDigit(no):
    Sum = 0
    rem = 0
    if(no == 0):
        return 0
    while(no > 0):
        rem = no % 10
        Sum = Sum + rem
        no = no // 10
    return Sum



def main():
    Number = int(input("Enter Number  : "))

    Count = SumOfDigit(Number)
    print(Count)

if __name__ == "__main__":
    main()