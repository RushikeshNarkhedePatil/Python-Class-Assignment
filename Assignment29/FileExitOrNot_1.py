# Q1) Check File Exists in Current Directory
# Problem Statement:
# Write a program which accepts a le name from the user and checks whether that le exists in the current
# directory or not.
# Input:
# Demo.txt
# Expected Output:
# Display whether Demo.txt exists or not.

import os

def check_file_exists(filename):
    # Check if the file exists in the current directory
    if os.path.isfile(filename):
        print(f"The file '{filename}' exists in the current directory.")
    else:
        print(f"The file '{filename}' does not exist in the current directory.")


def main():
    # Accept file name from the user
    file_name = input("Enter the file name to check: ")
    check_file_exists(file_name)

if __name__ == "__main__":
    main()