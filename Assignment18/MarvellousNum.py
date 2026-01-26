def Factor(no):
    count =0
    for i in range(1,no+1):
        if(no % i == 0):
            count = count + 1
    return count

def CheckPrime(No):
    count = Factor(No)
    if(count == 2):
        return True
    else:
        return False