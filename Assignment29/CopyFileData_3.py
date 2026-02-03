# Q3) Copy File Contents into a New File (Command Line)
# Problem Statement:
# Write a program which accepts an existing file name through command line arguments, creates a new file
# named Demo.txt, and copies all contents from the given file into Demo.txt.
# Input (Command Line):
# ABC.txt
# Expected Output:
# Create Demo.txt and copy contents of ABC.txt into Demo.txt.

import os
import sys

def copy_file_contain(FileName):
    if(os.path.isfile(FileName)):
        FileName = os.path.abspath(FileName)
    else:
        print("There is no file available")
        return
    
    # Open file
    fobj = open(FileName,"r")
    #read  file
    data = fobj.read()

    # write data in another file

    # Open new File

    fobj = open("Demo.txt","w")

    Ret = fobj.write(data)

    print("Number of bytes write in file : ",Ret)



    


def main():
    if(len(sys.argv)> 1):
        copy_file_contain(sys.argv[1])
    else:
        print(f"Please provide file name as a command line input")

    


if __name__ =="__main__":
    main()