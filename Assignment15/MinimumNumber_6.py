# 6. Write a lambda function using reduce() which accepts a list of numbers and returns the minimum
# element.

from functools import reduce

MinimumNumber = lambda No1,No2: No1 if No1 < No2 else No2
def main():
    numbers = [11,51,25,65,88,44,66]
    print(reduce(MinimumNumber,numbers))

if __name__ == "__main__":
    main()