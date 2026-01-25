# 1. Write a program which accepts length and width of rectangle and prints area.

def PrintArea(length, width):
    print("Area of Rectangle is :",length * width)


def main():
    Length = int(input("Enter Length : "))
    Width = int(input("Enter Width : "))
    
    PrintArea(Length,Width)

if __name__ == "__main__":
    main()