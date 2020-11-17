import math

def isPrime(num):
    if(num==2 or num==3 or num==5 or num==7):
        return 1
    if(num%2==0 or num==1):
        return 0
    i=1
    while(i<math.ceil(math.sqrt(num))):
        i+=2
        
        if(num%i==0):
            return 0
    return 1

aux=0
for x in range(2*pow(10,6)):
    if(isPrime(x)==1):
        aux+=x

print(aux)