# 8. Write a lambda function which accepts two numbers and returns addition.

Addition = lambda No1, No2 : No1 + No2

def main():
    number1 = int(input("Enter Number1 : "))
    number2 = int(input("Enter Number2 : "))
    print("Addition of Number is : ",Addition(number1,number2))

if __name__ == "__main__":
    main()