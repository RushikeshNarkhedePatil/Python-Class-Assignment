# 4. Write a program which accepts one number and prints all even numbers till that
# number.
# Input: 10
# Output: 2 4 6 8 10

def PrintEven(no):
    for i in range(2,no+1):
        if(i % 2 == 0):
            print(i,end=" ")

    print()


def main():
    Number = int(input("Enter Number : "))

    PrintEven(Number)

if __name__ == "__main__":
    main()