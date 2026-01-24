# 5. Write a lambda function using reduce() which accepts a list of numbers and returns the maximum
# element.
from functools import reduce

MaximumNumber = lambda No1,No2: No1 if No1 > No2 else No2
def main():
    numbers = [11,51,25,65,88,44,66]
    print(reduce(MaximumNumber,numbers))

if __name__ == "__main__":
    main()