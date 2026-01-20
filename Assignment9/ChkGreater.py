# write a program which contains one function named as ChkGreater which accepts two parameters and it should return greater number out of two numbers.
def ChkGreater(No1, No2):
    if No1 > No2:
        return No1
    else:
        return No2

def main():
    print("Enter first number:")
    Value1 = int(input())
    print("Enter second number:")
    Value2 = int(input())

    Result = ChkGreater(Value1, Value2)
    print("Greater number is:", Result)
    
# Starting point of the script
if __name__ == "__main__":
    main()