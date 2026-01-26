# 10. Write a program which accept number from user and return addition of digits in that number.
# Input : 5187934
# Output : 37

def CountDigit(No):
    sum = 0
    digit  = 0
    while(No > 0):
        digit = No % 10
        sum = sum + digit
        No = No //10
    return sum

def main():
    no = int(input("Enter Number : "))
    Ret = CountDigit(no)
    print("Addition of digit is : ",Ret)

if __name__ == "__main__":
    main()