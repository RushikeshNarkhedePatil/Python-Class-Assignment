# 8. Write a program which accept number from user and print that number of “*” on screen.
# Input : 5
# Output : * * * * *

def PrintStars(count):
    for _ in range(count):
        print("*", end=" ")
    print()  # For newline after printing all stars

def main():
    number = int(input("Enter a number: "))
    PrintStars(number)

if __name__ == "__main__":
    main()