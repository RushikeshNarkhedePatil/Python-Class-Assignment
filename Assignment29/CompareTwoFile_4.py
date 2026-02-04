# Q4) Compare Two Files (Command Line)
# Problem Statement:
# Write a program which accepts two le names through command line arguments and compares the contents of
# both les.
# •If both les contain the same contents, display Success
# •Otherwise display Failure

# Input (Command Line):
# Demo.txt Hello.txt
# Expected Output:
# Success OR Failure

import os
import sys

def compare_files(File1,File2):
    # Check both files exits or not
    if(os.path.exists(File1) and os.path.exists(File2)):
        File1 = os.path.abspath(File1)
        File2 = os.path.abspath(File2)
    else:
        print("There is no file available, check file availability")
        return
    
    File1Data = None
    File2Data = None

    if(os.path.isfile(File1)):
        fobj1 = open(File1,"r")
        File1Data = fobj1.read()

        #Close file
        fobj1.close()
    else:
        print("There is no such file : ",File1)

    if(os.path.isfile(File2)):
        fobj2 = open(File2,"r")
        File2Data = fobj2.read()

        #Close file
        fobj1.close()
    else:
        print("There is no such file : ",File2)

    # Compare both file data

    if(File1Data == File2Data):
        print("Both file is same data")
    else:
        print("File Contain not same")


def main():
    if(len(sys.argv) > 1):
        compare_files(sys.argv[1],sys.argv[2])

if __name__ =="__main__":
    main()


    

    
