# 2: Write a Python program to implement a class named Circle with the following
# requirements:

# •The class should contain three instance variables: Radius, Area, and Circumference.
# •The class should contain one class variable named PI, initialized to 3.14.
# •De ne a constructor (__init__) that initializes all instance variables to 0.0.
# •Implement the following instance methods:
# ◦Accept() – accepts the radius of the circle from the user.
# ◦CalculateArea() – calculates the area of the circle and stores it in the Area variable.
# ◦CalculateCircumference() – calculates the circumference of the circle and stores it in
# the Circumference variable.
# Display() – displays the values of Radius, Area, and Circumference.
# Create multiple objects of the Circle class and invoke all the instance methods for each object.

class Circle:
    PI = 3.14  # Class variable

    def __init__(self):
        self.Radius = 0.0  # Instance variable
        self.Area = 0.0    # Instance variable
        self.Circumference = 0.0  # Instance variable

    def Accept(self):
        self.Radius = float(input("Enter the radius of the circle: "))

    def CalculateArea(self):
        self.Area = Circle.PI * (self.Radius ** 2)

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print(f"Radius: {self.Radius}")
        print(f"Area: {self.Area}")
        print(f"Circumference: {self.Circumference}")

def main():
    num_circles = int(input("Enter the number of circles: "))
    circles = []

    for i in range(num_circles):
        print(f"\nCircle {i + 1}:")
        circle = Circle()
        circle.Accept()
        circle.CalculateArea()
        circle.CalculateCircumference()
        circle.Display()
        circles.append(circle)

if __name__ == "__main__":
    main()