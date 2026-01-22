# 7. Write a lambda function which accepts one number and returns True if divisible by 5.

DivisibleBy5 = lambda No : True if No %5 == 0 else False

def main():
    number = int(input("Enter Number to check Divisible by 5 : "))
    print(DivisibleBy5(number))

if __name__ == "__main__":
    main()