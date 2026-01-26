# 6. Write a program which accept one number and display below pattern.
# Input :
# 5
# Output : *  *   *   *   *
#          *  *   *   *
#          *  *   *
#          *  *
#          *

def DisplayStarPattern(No):
    for i in range(No):
        for j in range(No - i):
            print("*", end="  ")
        print()

def main():
    no = int(input("Enter Number : "))
    DisplayStarPattern(no)

if __name__ == "__main__":
    main()