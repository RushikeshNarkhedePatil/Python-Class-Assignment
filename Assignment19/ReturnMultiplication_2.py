# 2.Write a program which contains one lambda function which accepts two parameters and return
# its multiplication.
# Input : 4 3
# Output : 12

# Input : 6 3
# Output : 18

multiplication = lambda no1 , no2 : no1 * no2
def main():

    no1 = int(input("Enter 1st Number : "))
    no2 = int(input("Enter 2nd Number : "))
    Result = multiplication(no1,no2)
    print("multiplication of", no1, "and", no2, "is :", Result)

if __name__ == "__main__":
    main()