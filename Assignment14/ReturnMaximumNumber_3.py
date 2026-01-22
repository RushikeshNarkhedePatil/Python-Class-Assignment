# 3. Write a lambda function which accepts two numbers and returns maximum number.

MaximumNumber = lambda No1,No2 : No1 if No1 >= No2 else No2

def main():
    number1 = int(input("Enter First Number : "))
    number2 = int(input("Enter Second Number : "))
    result = MaximumNumber(number1,number2)
    print("The Maximum number is : ",result)

if __name__ == "__main__":
    main()