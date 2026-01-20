# 1. Write a program which accepts one number and prints multiplication table of that
# number.
# Input: 4
# Output:
# 4 8 12 16 20 24 28 32 36 40

def MultiplicationTable(No):
    for i in range(No,(No*10)+1,No):
        print(i,end=" ")
    print("\n")

def main():
    Number = int(input("Enter Number to print table : "))

    MultiplicationTable(Number)

if __name__ == "__main__":
    main()