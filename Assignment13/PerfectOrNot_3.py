# 3. Write a program which accepts one number and checks whether it is perfect number or
# not.
# Input: 6
# Output: Perfect Number

def PerfectOrNot(no):
    stop = no // 2
    temp = 0

    for i in range(1,stop+1):
        temp = temp + i
        if(temp == no):
            return True
        elif(temp > no):
            return False

    return False
        
def main():
    No = int(input("Enter number : "))
    flag = PerfectOrNot(No)
    if(flag):
        print(No," : is  Perfect Number")
    else:
        print(No," : is not perfect number")

if __name__ =="__main__":
    main()
        
        