def sumPowFiveNum(n):
    number=0
    i=1
    while(n-i>0):
        number+=pow((int(str(int(n/i))[-1])),5)
        i*=10
    return number

def solution():
    i=2
    result=0
    while(i<9999999):
        if(sumPowFiveNum(i)==i):
            print i
            result+=i
        i+=1
    return result

print solution()