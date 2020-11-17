from decimal import *
getcontext().prec = 10000

def getLenRecurringCycle(n):
    while(n%2==0):
        n/=2
    while(n%5==0):
        n/=5
    #look if number is terminal
    i=1
    while(i<n):
        if(pow(10,i)%n==0):
            return 0
        i+=1
    #look if number is completely repeating
    i=1
    while(i<n):
        if(pow(10,i)%n==1):
            return i
        i+=1
    #look if number is repeating after a part
    i=1
    while(i<n):
        if(pow(10,i)%n==1):
            return i
        i+=1

def solution():
    i=1
    aux1=0
    aux2=0
    result=0
    while(i<1000):
        aux1=getLenRecurringCycle(i)
        if(aux1>aux2):
            aux2=aux1
            result=i
        i+=1
    
    return result
        
    
print solution()