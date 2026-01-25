# 7. Write a program which contains one function that accept one number from user and returns
# true if number is divisible by 5 otherwise return false.
# Input : 8
# Output : False
# Input : 25
# Output : True

def IsDivisibleBy5(num):
    if num % 5 == 0:
        return True
    else:
        return False
    
def main():
    number = int(input("Enter a number: "))
    if IsDivisibleBy5(number):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()