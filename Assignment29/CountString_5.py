# Q5) Frequency of a String in File
# Problem Statement:
# Write a program which accepts a le name and one string from the user and returns the frequency (count of
# occurrences) of that string in the le.
# Input:
# Demo.txt Marvellous
# Expected Output:
# Count how many times "Marvellous" appears in Demo.txt.

import os
def count_string(FileName,Str):
    # Check file exits or not
    if(os.path.exists(FileName)):
        FileName = os.path.abspath(FileName)
    else:
        print("There is no file available, check file availability")
        return
    
    if(os.path.isfile(FileName)):
        fobj = open(FileName,"r")
        FileData = fobj.read()

        #Close file
        fobj.close()
    else:
        print("There is no such file : ",FileName)

    # Count string in file data
    Count = FileData.count(Str)
    print("String {} appears {} times in file {}".format(Str,Count,FileName))

def main():
    FileName = input("Enter file name : ")
    Str = input("Enter string to count : ")
    count_string(FileName,Str)

if __name__ =="__main__":
    main()