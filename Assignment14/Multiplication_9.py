# 9. Write a lambda function which accepts two numbers and returns multiplication.
Multiplication = lambda No1 , No2 : No1 * No2 

def main():
    number1 = int(input("Enter Number1 : "))
    number2 = int(input("Enter Number2 : "))
    print("Multiplication of Number is : ",Multiplication(number1,number2))

if __name__ == "__main__":
    main()