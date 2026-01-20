# 3. Write a program which accepts one number and prints factorial of that number.
# Input: 5
# Output: 120

def Factorial(no):
    Fact = 1
    for i in range(1,no+1):
        Fact = Fact * i
    return Fact


def main():
    Number = int(input("Enter Number : "))

    Fact = Factorial(Number)
    print("Factorial of numbers is : ",Fact)

if __name__ == "__main__":
    main()