# 4.Write a program which accept one number form user and return addition of its factors.
# Input : 12
# Output : 16
# (1+2+3+4+6)

def AdditopnOfFactor(No):
    sum =0
    for i in range(1,No):
        if(No % i == 0):
            sum = sum +i

    return sum

def main():
    no = int(input("Enter Number : "))
    Ret = 0
    Ret = AdditopnOfFactor(no)
    print(f"Addition of Factor {no} is : ",Ret)

if __name__ == "__main__":
    main()