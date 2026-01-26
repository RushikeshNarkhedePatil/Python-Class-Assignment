# 3.Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all such numbers which greater than or equal to 70 and less than or equal to
# 90. Map function will increase each number by 10. Reduce will return product of all that
# numbers.
# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter = [76, 89, 86, 90, 70]
# List after map = [86, 99, 96, 100, 80]
# Output of reduce = 6538752000

from functools import reduce

def FilterFunction(no):
    if(no >= 70 and no <= 90):
        return True
    else:
        return False
    
def MapFunction(no):
    return no + 10

def ReduceFunction(a,b):
    return a * b

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