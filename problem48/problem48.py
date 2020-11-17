def solution():
    i=1
    result=0
    while(i<1001):
        result+=pow(i,i)
        i+=1
    
    return result

print solution()