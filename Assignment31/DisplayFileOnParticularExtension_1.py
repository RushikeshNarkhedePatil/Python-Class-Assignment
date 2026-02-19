# Please follow below rules while designing automation script as
# • Accept input through command line or through file.
# • Display any message in log file instead of console.
# • For separate task define separate function.
# • For robustness handle every expected exception.
# • Perform validations before taking any action.
# • Create user defined modules to store the functionality.
# 1.Design automation script which accept directory name and file extension from user. Display all
# files with that extension.
# Usage : DirectoryFileSearch.py “Demo” “.txt”
# Demo is name of directory and .txt is the extension that we want to search.

import os
import time
import sys

def display_files_with_extension(DirName,Extension):
    # Check directory exits or not
    if(os.path.exists(DirName)):
        DirName = os.path.abspath(DirName)
    else:
        print("There is no such directory : ",DirName)
        return
    
    #open file to store log
    time_stamp = time.strftime("%Y-%m-%d %H:%M:%S")
    Border = "-" * 100
    LogFile = open(f"LogFile_{time_stamp}.txt","a")
    LogFile.write(Border + "\n")
    LogFile.write("Directory name : {} and Extension : {} \n".format(DirName,Extension))


    if(os.path.isdir(DirName)):
        LogFile.write("Files with extension {} in directory {} are : \n".format(Extension,DirName))
        LogFile.write(Border + "\n")   
        for Foldername,Subfolder,Filename in os.walk(DirName):
            for File in Filename:
                if(File.endswith(Extension)):
                    LogFile.write(File + "\n")
        LogFile.write(Border + "\n")
        LogFile.close()
    else:
        print("There is no such directory : ",DirName)

def main():
    if(len(sys.argv) != 3):
        print("Invalid number of arguments")
        print("Usage : DirectoryFileSearch.py “Demo” “.txt”")
        return
    DirName = sys.argv[1]
    Extension = sys.argv[2]
    display_files_with_extension(DirName,Extension)

if __name__ =="__main__":
    main()