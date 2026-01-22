# 4. Write a lambda function which accepts two numbers and returns minimum number.

MinimumNumber = lambda No1,No2 : No1 if No1 < No2 else No2

def main():
    number1 = int(input("Enter First Number : "))
    number2 = int(input("Enter Second Number : "))
    result = MinimumNumber(number1,number2)
    print("The Minimum number is : ",result)

if __name__ == "__main__":
    main()