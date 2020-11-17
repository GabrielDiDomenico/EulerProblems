def nextTriangularNum(n):
    return n*(n+1)/2

def factors(x):
    result=0
    i=1

    while(i*i <= x):
        if(x % i == 0):
            result+=1
            if(x//i != i):
                result+=1
        i += 1
   
    return result

def solution():
    num=1
    index=1
    while(factors(num)<500):
        index+=1
        num=nextTriangularNum(index)
    return num

print(solution())