# write a program which accepts one number and check whether it is divisible by 3 and 5
def DivisibleBy3and5(No):
    if (No % 3 == 0) and (No % 5 == 0):
        return True
    else:
        return False
    
def main():
    print("Enter number:")
    Value = int(input())

    Result = DivisibleBy3and5(Value)
    if Result == True:
        print("Number is divisible by 3 and 5")
    else:
        print("Number is not divisible by 3 and 5")

# Starting point of the script
if __name__ == "__main__":
    main()