# 1. Write a lambda function which accepts one number and returns square of that number.
square = lambda x: x ** 2


def main():
    number = int(input("Enter Number : "))
    result = square(number)
    print(f"The square of {number} is {result}")

if __name__ == "__main__":
    main()