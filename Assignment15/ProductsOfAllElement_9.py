# 9. Write a lambda function using reduce() which accepts a list of numbers and returns the product of all
# elements.
from functools import reduce
Multiplication = lambda number1, number2 : number1 * number2

def main():
    Data = [5,5,55,88]
    print(reduce(Multiplication,Data))
    
if __name__ == "__main__":
    main()
    