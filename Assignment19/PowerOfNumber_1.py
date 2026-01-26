# 1.Write a program which contains one lambda function which accepts one parameter and return
# power of two.
# Input : 4
# Output : 16

# Input : 6
# Output : 64

PowerOfTwo = lambda No: No ** 2

def main():

    no = int(input("Enter Number : "))
    Result = PowerOfTwo(no)
    print("Power of", no, "is :", Result)

if __name__ == "__main__":
    main()