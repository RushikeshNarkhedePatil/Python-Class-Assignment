# 5.Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
# return Maximum number from that numbers. (You can also use normal functions instead of
# lambda functions).
# Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
# List after filter = [2, 11, 17, 23, 31]
# List after map = [4, 22, 34, 46, 62]
# Output of reduce = 62

from functools import reduce

def FilterFunction(no):
    if no < 2:
        return False
    for i in range(2, int(no**0.5) + 1):
        if no % i == 0:
            return False
    return True

def MapFunction(no):
    return no * 2
def ReduceFunction(a, b):
    if a > b:
        return a
    else:
        return b
    
def main():
    Numbers = []
    no = int(input("Enter number of count to add on list : "))

    for _ in range(no):
        No = int(input())
        Numbers.append(No)

    print("Input List : ", Numbers)

    FilteredList = list(filter(FilterFunction, Numbers))
    print("List after filter : ", FilteredList)

    MappedList = list(map(MapFunction, FilteredList))
    print("List after map : ", MappedList)

    ReducedValue = reduce(ReduceFunction, MappedList)
    print("Output of reduce : ", ReducedValue)

if __name__ == "__main__":
    main()