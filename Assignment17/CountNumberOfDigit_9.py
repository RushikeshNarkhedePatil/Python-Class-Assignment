# 9. Write a program which accept number from user and return number of digits in that number.
# Input : 5187934
# Output : 7

def CountDigit(No):
    icnt = 0
    while(No > 0):
        icnt = icnt + 1
        No = No //10
    return icnt

def main():
    no = int(input("Enter Number : "))
    Ret = CountDigit(no)
    print("Number of digit count is : ",Ret)

if __name__ == "__main__":
    main()