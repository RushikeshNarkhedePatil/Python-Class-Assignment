# 2. Write a program which accept one number and display below pattern.
# Input :
# 5
# Output :
# * * * * *
# * * * * *
# * * * * *
# * * * * * 
# * * * * *

def DisplayPattern(No):
    for i in range(No):
        for j in range(No):
            print("* ", end=" ")
        print()  # Move to new line after complete row.

def main():
    No = int(input("Enter number to print pattern : "))
    DisplayPattern(No)
if __name__ == "__main__":
    main()