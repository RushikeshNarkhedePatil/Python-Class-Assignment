# 5. Write a program which accepts one number and checks whether it is palindrome or not.
# Input: 121
# Output: Palindrome

def PalindromeOrNot(no):
    Rev = 0
    Digit = 0
    temp = no
    if(no == 0):
        return 0
    while(no > 0):
        Digit = no % 10
        Rev = (Rev *10) + Digit 
        no = no // 10

    if(temp == Rev):
        return True
    else:
        False


def main():
    Number = int(input("Enter Number: "))

    Status = PalindromeOrNot(Number)
    if(Status):
        print("Number is Palindrome :",Number)
    else:
        print("Number is not palindrome : ",Number)

if __name__ == "__main__":
    main()