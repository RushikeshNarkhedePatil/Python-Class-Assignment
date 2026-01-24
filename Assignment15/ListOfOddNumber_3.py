# 3. Write a lambda function using filter() which accepts a list of numbers and returns a list of odd
# numbers.

ListOfEvenNumber = lambda numbers : numbers % 2!=0

numbers =[10,5,44,45,66,78]
def main():
    print(list(filter(ListOfEvenNumber,numbers)))

if __name__ =="__main__":
    main()