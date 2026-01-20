# write a program which accepts one number and print square of that number.
def SquareOfNumber(No):
    return No * No
def main():
    print("Enter number:")
    Value = int(input())

    Result = SquareOfNumber(Value)
    print("Square of number is:", Result)

# Starting point of the script
if __name__ == "__main__":
    main()