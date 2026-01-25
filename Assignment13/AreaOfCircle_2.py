# 2. Write a program which accepts radius of circle and prints area of circle.

def AreaOfCircle(radius):
    p = 3.14

    print("Area of Circle is : ",p * (radius * radius))


def main():
    area=int(input("Enter area: "))
    AreaOfCircle(area)

if __name__ == "__main__":
    main()