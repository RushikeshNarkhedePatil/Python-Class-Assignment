# 3: Write a Python program to implement a class named Arithmetic with the following
# characteristics:
# •The class should contain two instance variables: Value1 and Value2.
# •De ne a constructor (__init__) that initializes all instance variables to 0.
# •Implement the following instance methods:
# ◦Accept() – accepts values for Value1 and Value2 from the user.
# ◦Addition() – returns the addition of Value1 and Value2.
# ◦Subtraction() – returns the subtraction of Value1 and Value2.
# ◦Multiplication() – returns the multiplication of Value1 and Value2.
# ◦Division() – returns the division of Value1 and Value2 (handle division by zero
# properly).
# Create multiple objects of the Arithmetic class and invoke all the instance methods.

class Arithmetic:
    def __init__(self):
        self.Value1 = 0  # Instance variable
        self.Value2 = 0  # Instance variable

    def Accept(self):
        self.Value1 = float(input("Enter Value1: "))
        self.Value2 = float(input("Enter Value2: "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if self.Value2 != 0:
            return self.Value1 / self.Value2
        else:
            return "Error: Division by zero is not allowed."
        
def main():
    num_objects = int(input("Enter the number of Arithmetic objects to create: "))
    arithmetic_objects = []

    for i in range(num_objects):
        print(f"\nArithmetic Object {i + 1}:")
        arithmetic = Arithmetic()
        arithmetic.Accept()
        print("Addition:", arithmetic.Addition())
        print("Subtraction:", arithmetic.Subtraction())
        print("Multiplication:", arithmetic.Multiplication())
        print("Division:", arithmetic.Division())
        arithmetic_objects.append(arithmetic)

if __name__ == "__main__":
    main()