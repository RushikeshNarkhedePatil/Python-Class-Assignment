# write a program which accepts one number from user and print cube of that number.
def CubeOfNumber(No):
    print("Cube of number is:", No * No * No)
def main():
    print("Enter number:")
    Value = int(input())

    CubeOfNumber(Value)

# Starting point of the script
if __name__ == "__main__":
    main()