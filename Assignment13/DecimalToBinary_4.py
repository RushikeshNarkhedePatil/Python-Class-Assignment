# 4. Write a program which accepts one number and prints binary equivalent.

def DecimalToBinary(no):
    digit = 0
    rev = list()
    while(no != 0):
        digit = no % 2
        #print(digit)
        rev.append(digit)
        no = no // 2
    l = len(rev)
    for i in range(l):
        print(rev[(l-i-1)],end="")
    print()
        

def main():
    No = int(input("Enter Number : "))
    DecimalToBinary(No)

if __name__ == "__main__":
    main()


