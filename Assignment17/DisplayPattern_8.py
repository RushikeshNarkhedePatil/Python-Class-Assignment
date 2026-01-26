# 8. Write a program which accept one number and display below pattern.
# Input :
# 5
# Output :
# 1
# 1   2
# 1   2   3
# 1   2   3   4
# 1   2   3   4   5

def DisplayPattern(No):
    for i in range(No+1):
        for j in range(1, No + 1):
            if(i >=j):
                print(j, end="   ")
        print()

def main():
    no = int(input("Enter Number : "))
    DisplayPattern(no)

if __name__ == "__main__":
    main()