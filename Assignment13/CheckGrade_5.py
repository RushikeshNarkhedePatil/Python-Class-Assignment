# 5. Write a program which accepts marks and displays grade.
# Condition Example:
# •≥ 60 → First Class
# •≥ 50 → Second Class
# •< 50 → Fail
# ≥ 75 → Distinction

def DisplayGrade(mark):
    if mark >= 75:
        print("Distinction")
    elif mark >=60:
        print("First Class")
    elif mark >= 50:
        print("Second Class")
    elif mark < 50:
        print("Fail")

def main():
    Mark = int(input("Enter Marks : "))
    DisplayGrade(Mark)

if __name__ == "__main__":
    main()