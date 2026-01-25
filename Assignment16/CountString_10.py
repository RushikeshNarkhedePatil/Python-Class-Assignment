# 10. Write a program which accept name from user and display length of its name.
# Input : Marvellous
# Output : 10
# Note :
# For each above question please create separate .py file as
# Assignment1_1.py
# Assignment1_2.py
# Assignment1_3.py
# Every applications logic should be enclosed in function.

def DisplayLengthOfString(Name):
    icnt = 0
    for i in Name:
        icnt =  icnt + 1

    print(icnt)

def main():
    name = input("Enter Name to Count : ")
    DisplayLengthOfString(name)

if __name__ == "__main__":
    main()
