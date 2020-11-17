def collatzSeq(n,x):
    count=x
    if(n==1):
        return count
    else:
        if(n%2==0):
            return collatzSeq(n/2,count+1)
        else:
            return collatzSeq(3*n+1,count+1)

def solution():
    i=pow(10,6)
    seq=0
    aux=0
    result=0
    while(i>1):
        aux=collatzSeq(i,1)
        if(aux>seq):
            seq=aux
            result=i
        i-=1
    return result


print(solution())