# 2. Write a lambda function which accepts one number and returns cube of that number.
Cube= lambda No : No * No * No

def main():
    number = int(input("Enter Number : "))
    result = Cube(number)
    print(f"The Cube of {number} is {result}")

if __name__ == "__main__":
    main()