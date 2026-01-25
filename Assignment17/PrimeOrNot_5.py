# 5.Write a program which accept one number for user and check whether number is prime or not.
# Input : 5

def Factor(no):
    count =0
    for i in range(1,no+1):
        if(no % i == 0):
            count = count + 1
    return count

def PrimeOrNot(No):
    count = Factor(No)
    if(count == 2):
        return True
    else:
        return False

def main():
    no = int(input("Enter Number : "))
    status = PrimeOrNot(no)

    if(status):
        print(no ," is Prime Number")
    else:
        print(no," is Not Prime Number")

if __name__ == "__main__":
    main()