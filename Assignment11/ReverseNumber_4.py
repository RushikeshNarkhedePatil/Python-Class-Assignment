# 4. Write a program which accepts one number and prints reverse of that number.
# Input: 123
# Output: 321

def ReverseNumber(no):
    Rev = ""
    Digit = 0
    if(no == 0):
        return 0
    while(no > 0):
        Digit = no % 10
        Sum = Sum + Digit
        no = no // 10
    return Sum



def main():
    Number = int(input("Enter Number: "))

    Count = ReverseNumber(Number)
    print(Count)

if __name__ == "__main__":
    main()