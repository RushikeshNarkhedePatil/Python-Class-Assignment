# Q2) Display File Contents
# Problem Statement:
# Write a program which accepts a le name from the user, opens that le, and displays the entire contents on the
# console.
# Input:
# Demo.txt
# Expected Output:
# Display contents of Demo.txt on console.
import os

def display_file_contain(FileName):

    # File Present or not
    if(os.path.isfile(FileName)):
        FileName=os.path.abspath(FileName)


    # Open File
    fobj = open(FileName,"r")
    #read File
    data = fobj.read()
    #Display File Data
    print("File Data is : ",data)
def main():
    # Accept file name from the user
    file_name = input("Enter the file name : ")
    display_file_contain(file_name)

if __name__ == "__main__":
    main()

