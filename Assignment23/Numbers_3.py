# 3: Write a Python program to implement a class named Numbers with the following
# speci cations:
# •
# The class should contain one instance variable:
# ◦Value
# •De ne a constructor (__init__) that accepts a number from the user and initializes Value.
# •Implement the following instance methods:
# ◦ChkPrime() – returns True if the number is prime, otherwise returns False
# ◦ChkPerfect() – returns True if the number is perfect, otherwise returns False
# ◦Factors() – displays all factors of the number
# ◦SumFactors() – returns the sum of all factors
# (You may use this method as a helper in ChkPerfect() if required)
# Create multiple objects and call all methods.


class Numbers:
    def __init__(self, Value):
        self.Value = Value  # Instance variable for the number

    def ChkPrime(self):
        # Check if the number is prime
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value**0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        # Check if the number is perfect
        sum_of_factors = self.SumFactors()
        return sum_of_factors == self.Value

    def Factors(self):
        # Display all factors of the number
        factors = []
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                factors.append(i)
        print(f"Factors of {self.Value}: {factors}")

    def SumFactors(self):
        # Return the sum of all factors
        sum_of_factors = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum_of_factors = sum_of_factors + i
        return sum_of_factors
    

# Create instances of Numbers and demonstrate all methods
num1 = Numbers(28)
print(f"Is {num1.Value} prime? {num1.ChkPrime()}")  # Output: Is 28 prime? False
print(f"Is {num1.Value} perfect? {num1.ChkPerfect()}")  # Output: Is 28 perfect? True
num1.Factors()  # Output: Factors of 28: [1, 2, 4, 7, 14, 28]
print(f"Sum of factors of {num1.Value}: {num1.SumFactors()}")  # Output: Sum of factors of 28: 56