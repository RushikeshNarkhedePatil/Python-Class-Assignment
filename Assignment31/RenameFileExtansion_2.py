# 2. Design automation script which accept directory name and two file extensions from user.
# Rename all files with first file extension with the second file extenntion.

import os
import sys

def rename_file_extension(DirName,Extension1,Extension2):
    # Check directory exits or not
    if(os.path.exists(DirName)):
        DirName = os.path.abspath(DirName)
    else:
        print("There is no such directory : ",DirName)
        return
    
    if(os.path.isdir(DirName)):
        for Foldername,Subfolder,Filename in os.walk(DirName):
            for File in Filename:
                if(File.endswith(Extension1)):
                    OldFilePath = os.path.join(Foldername,File)
                    NewFilePath = os.path.join(Foldername,File.replace(Extension1,Extension2))
                    os.rename(OldFilePath,NewFilePath)
    else:
        print("There is no such directory : ",DirName)

def main():
    if(len(sys.argv) != 4):
        print("Invalid number of arguments")
        print("Usage : RenameFileExtansion.py “Demo” “.txt” “.doc”")
        return
    DirName = sys.argv[1]
    Extension1 = sys.argv[2]
    Extension2 = sys.argv[3]
    rename_file_extension(DirName,Extension1,Extension2)

if __name__ =="__main__":
    main()