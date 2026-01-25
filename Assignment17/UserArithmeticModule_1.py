# 1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
# for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
# parameters as number and perform the operation. Write on python program which call all the
# functions from Arithmetic module by accepting the parameters from user.

import Arithmetic

def main():
    print("Enter first number : ")
    No1 = int(input())

    print("Enter second number : ")
    No2 = int(input())

    Ret = Arithmetic.Add(No1,No2)
    print("Addition is : ",Ret)

    Ret = Arithmetic.Sub(No1,No2)
    print("Subtraction is : ",Ret)

    Ret = Arithmetic.Mult(No1,No2)
    print("Multiplication is : ",Ret)

    Ret = Arithmetic.Div(No1,No2)
    print("Division is : ",Ret)

if __name__ == "__main__":
    main()