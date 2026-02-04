# Q2) Count Words in a File
# Problem Statement:
# Write a program which accepts a file name from the user and counts the total number of words in that file.
# Input:
# Demo.txt
# Expected Output:
# Total number of words in Demo.txt.

import os

def count_words(FileName):
    # Check file exits or not
    if(os.path.exists(FileName)):
        FileName = os.path.abspath(FileName)
    else:
        print("There is no file available, check file availability")
        return
    
    if(os.path.isfile(FileName)):
        fobj = open(FileName,"r")
        WordCount = 0

        for line in fobj:
            words = line.split()
            WordCount = WordCount + len(words)

        #Close file
        fobj.close()
    else:
        print("There is no such file : ",FileName)

    print("Total number of words in file {} is : {}".format(FileName,WordCount))

def main():
    FileName = input("Enter file name : ")
    count_words(FileName)

if __name__ =="__main__":
    main()