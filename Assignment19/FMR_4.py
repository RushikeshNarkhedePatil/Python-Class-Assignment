# 4.Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all such numbers which are even. Map function will calculate its square.
# Reduce will return addition of all that numbers.
# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204

from functools import reduce

def FilterFunction(no):
    if(no % 2 == 0):
        return True
    else:
        return False
    
def MapFunction(no):
    return no * no

def ReduceFunction(a,b):
    return a + b

def main():
    Numbers = []
    no = int(input("Enter number of count to add on list : "))

    for _ in range(no):
        No = int(input())
        Numbers.append(No)

    print("Input List : ",Numbers)

    FilteredList = list(filter(FilterFunction, Numbers))
    print("List after filter : ",FilteredList)

    MappedList = list(map(MapFunction, FilteredList))
    print("List after map : ",MappedList)

    ReducedValue = reduce(ReduceFunction, MappedList)
    print("Output of reduce : ",ReducedValue)

if __name__ == "__main__":
    main()