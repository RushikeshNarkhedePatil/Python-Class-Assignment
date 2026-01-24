# 1. Write a lambda function using map() which accepts a list of numbers and returns a list of squares of
# each number.
SeuaresOfEachNumber = lambda numbers : numbers **2

def main():
    Numbers =[10,20,30,40,50]
    numbers = list(map(SeuaresOfEachNumber,Numbers))
    print("Seuares of each number is :",numbers)

if __name__ == "__main__":
    main()