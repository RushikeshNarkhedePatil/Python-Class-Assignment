# 1: Write a Python program to implement a class named BookStore with the following
# speci cations:
# •
# •
# The class should contain two instance variables:
# ◦Name (Book Name)
# ◦Author (Book Author)
# The class should contain one class variable:
# ◦
# NoOfBooks (initialize it to 0)
# •De ne a constructor (__init__) that accepts Name and Author and initializes instance variables.
# •Inside the constructor, increment the class variable NoOfBooks by 1 whenever a new object is
# created.
# •Implement an instance method:
# ◦
# Display() – should display book details in the format:
# <BookName> by <Author>. No of books: <NoOfBooks>
# Example usage:
# Obj1 = BookStore("Linux System Programming", "Robert Love")
# Obj1.Display()
# # Linux System Programming by Robert Love. No of
# books: 1
# Obj2 = BookStore("C Programming", "Dennis Ritchie")
# Obj2.Display()
# # C Programming by Dennis Ritchie. No of books: 2

class BookStore:
    NoOfBooks = 0  # Class variable to keep track of the number of books

    def __init__(self, Name, Author):
        self.Name = Name  # Instance variable for book name
        self.Author = Author  # Instance variable for book author
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1  # Increment the class variable when a new book is created

    def Display(self):
        # Display book details in the specified format
        print(f"{self.Name} by {self.Author}. No of books: {BookStore.NoOfBooks}")

# Create instances of BookStore and display their details :
Obj1 = BookStore("Linux System Programming", "Robert Love") 
Obj1.Display()  # Output: Linux System Programming by Robert Love. No of books: 1
Obj2 = BookStore("C Programming", "Dennis Ritchie")
Obj2.Display()  # Output: C Programming by Dennis Ritchie. No of books: 2
