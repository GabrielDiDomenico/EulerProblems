def units(num):
    if(num==1 or num==2 or num==6):
        return 3
    if(num==3 or num==7 or num==8):
        return 5
    if(num==4 or num==5 or num==9):
        return 4

def ten(num1,num2):
    if(num1==1):
        if(num2==0):
            return 3
        if(num2==1):
            return 6
        if(num2==2):
            return 6
        if(num2==3):
            return 8
        if(num2==4):
            return 8
        if(num2==5):
            return 7
        if(num2==6):
            return 7
        if(num2==7):
            return 9
        if(num2==8):
            return 8
        if(num2==9):
            return 8
    if(num1==2 or num1==3 or num1==8 or num1==9):
        if(num2==0):
            return 6
        else:
            return 6+units(num2)
    if(num1==4 or num1==5 or num1==6):
        if(num2==0):
            return 5
        else:
            return 5+units(num2)
    if(num1==7):
        if(num2==0):
            return 7
        else:
            return 7+units(num2)

def hundred(num1,num2,num3):
    if(num2==0 and num3==0):
        return 7+units(num1)
    if(num2==0 and num3!=0):
        return units(num1)+10+units(num3)
    else:
        return units(num1)+10+ten(num2,num3)

                
def solution():
    result=0
    for x in range(1,1000):
        if(x<10):
            result+=units(x)
        if(x>9 and x<100):
            result+=ten(int(str(int(x/10))[-1]),int(str(int(x/1))[-1]))
        if(x>99):
            result+=hundred(int(str(int(x/100))[-1]),int(str(int(x/10))[-1]),int(str(int(x/1))[-1]))

    return result+11

print(solution())