# Q1) Count Lines in a File
# Problem Statement:
# Write a program which accepts a file name from the user and counts how many lines are present in the file.
# Input:
# Demo.txt
# Expected Output:
# Total number of lines in Demo.txt.

import os
def count_lines(FileName):
    # Check file exits or not
    if(os.path.exists(FileName)):
        FileName = os.path.abspath(FileName)
    else:
        print("There is no file available, check file availability")
        return
    
    if(os.path.isfile(FileName)):
        fobj = open(FileName,"r")
        LineCount = 0

        for line in fobj:
            LineCount += 1

        #Close file
        fobj.close()
    else:
        print("There is no such file : ",FileName)

    print("Total number of lines in file {} is : {}".format(FileName,LineCount))

def main():
    FileName = input("Enter file name : ")
    count_lines(FileName)

if __name__ =="__main__":
    main()