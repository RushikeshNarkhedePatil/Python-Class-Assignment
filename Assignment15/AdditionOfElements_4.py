# 4. Write a lambda function using reduce() which accepts a list of numbers and returns the addition of
# all elements.

from functools import reduce

Addition = lambda A,B: A + B

def main():
    Numbers = [11,21,51,101,151,201]
    print(reduce(Addition,Numbers))

if __name__ == "__main__":
    main()