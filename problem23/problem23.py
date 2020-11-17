import math

def findSumDivisors(n) : 
    divisors=0
    i = 1
    while(i <= math.sqrt(n)): 
        if(n%i==0): 
            if (n/i==i): 
                divisors+=i
            else: 
                divisors+=i
                divisors+=n/i
        i+=1
    print divisors-n
    return divisors-n

def abudantNumber(num):
    if(findSumDivisors(num)>num):
        return True
    else:
        return False

def getListOfAbudantNumer():
    arr = []
    i=12
    while(i<15000):
        if(abudantNumber(i)):
            arr.append(i)
        i+=1

    return arr

def getListOfAllSums():
    arr = getListOfAbudantNumer()
    sumArr = [24]
    i=0
    while(i<len(arr)):
        j=i
        while(j<len(arr)):
            sumArr.append(arr[i]+arr[j])
            j+=1
        i+=1

    sumArr.sort()
    
    i=len(sumArr)-1
    while(i>0):
        if(sumArr[i]==sumArr[i-1]):
            sumArr.pop(i-1)
        i-=1
    return sumArr

def solution():
    result=0
    arr = getListOfAllSums()
    print arr
    i=0
    j=0
    while(i<28123):
        if(i<arr[j]):
            print i
            result+=i
        else:
            j+=1
        
        i+=1

    return result

print solution()



