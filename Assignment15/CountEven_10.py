# 10.Write a lambda function using filter() which accepts a list of numbers and returns the count of even
# numbers.

CountEven = lambda No : No %2 ==0

def main():
    data = [10,55,22,66]
    CountEvenData = list(filter(CountEven,data))
    print(len(CountEvenData))

if __name__ == "__main__":
    main()