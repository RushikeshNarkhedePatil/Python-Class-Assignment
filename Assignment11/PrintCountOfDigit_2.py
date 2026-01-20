# 2.Write a program which accepts one number and prints count of digits in that number.
# Input: 7521
# Output: 4

def CountDigit(no):
    count = 0
    while(no > 0):
        no = no // 10
        count = count + 1
    return count



def main():
    Number = int(input("Enter Number to print table : "))

    Count = CountDigit(Number)
    print(Count)

if __name__ == "__main__":
    main()