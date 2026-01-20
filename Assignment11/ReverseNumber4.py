# 4. Write a program which accepts one number and prints reverse of that number.
# Input: 123
# Output: 321

def ReverseNumber(no):
    Digit = 0
    if(no == 0):
        return 0
    while(no > 0):
        Digit = no % 10
        print(Digit,end="")
        no = no // 10

    print()



def main():
    Number = int(input("Enter Number: "))

    ReverseNumber(Number)

if __name__ == "__main__":
    main()