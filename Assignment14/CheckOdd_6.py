# 6. Write a lambda function which accepts one number and returns True if number is odd
# otherwise False.

Even= lambda No : True if No %2 != 0 else False

def main():
    number1 = int(input("Enter Number to check Odd number : "))
    print(Even(number1))

if __name__ == "__main__":
    main()