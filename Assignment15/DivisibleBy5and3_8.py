# 8. Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers
# divisible by both 3 and 5.

DivisibleBy5and3 = lambda Number : Number if Number %5==0 and Number %3 == 0 else 0

def main():
    data = [10,15,4,88,18]
    print(list(filter(DivisibleBy5and3,data)))

if __name__ == "__main__":
    main()