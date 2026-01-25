# 3. Write a program which accept one number from user and return its factorial.
# Input : 5  eg (5 * 4 * 3 * 2 * 1)
# Output : 120

def Factorial(No):
    Fact = 1

    for i in range(1,No+1):
        Fact = Fact * i

    return Fact

def main():
    Ret = 0
    no = int(input("Enter Number : "))
    Ret = Factorial(no)
    print(f"Factorial of {no} is : ",Ret)

if __name__ == "__main__":
    main()