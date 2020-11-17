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
        
    return divisors-n

def amicableNumber(num):
    div = findSumDivisors(num)
    if(findSumDivisors(div)==num and div!=num):
        return True
    else:
        return False

def solution():
    result=0
    for x in range(1,10000):
        if(amicableNumber(x)):
            result+=x
    
    return result

print solution()