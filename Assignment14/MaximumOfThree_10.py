# 10. Write a lambda function which accepts three numbers and returns largest number.

MaximumOfThreeNumber = lambda No1,No2,No3 : No1 if (No1 >= No2 and No1 >= No3)  else (No2 if No2 >= No1 and No2 >= No3 else No3)

def main():
    number1 = int(input("Enter First Number : "))
    number2 = int(input("Enter Second Number : "))
    number3 = int(input("Enter Third Number : "))
    result = MaximumOfThreeNumber(number1,number2,number3)
    print("The Minimum number is : ",result)

if __name__ == "__main__":
    main()