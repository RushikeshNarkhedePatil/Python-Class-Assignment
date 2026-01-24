# . Write a lambda function using filter() which accepts a list of strings and returns a list of strings
# having length greater than 5.

StringLengthGreterThanFive = lambda data : len(data) > 5

def main():
    Data = ["Jay Ganesh","Demo","Nano","Ujwal","Rushikesh"]
    print(list(filter(StringLengthGreterThanFive,Data)))

if __name__ =="__main__":
    main()