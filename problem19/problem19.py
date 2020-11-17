def solution():
    normalYear=[31,28,31,30,31,30,31,31,30,31,30,31]
    leapYear=[31,29,31,30,31,30,31,31,30,31,30,31]
    years=1901
    days=2
    count=0
    result=0
    while(years<2001):
        if(years%4==0):
            for x in leapYear:
                while(count<x):
                    if(days==0 and count==0):
                        result+=1
                    days+=1
                    if(days==7):
                        days=0
                    count+=1
                count=0
        else:
            for x in normalYear:
                while(count<x):
                    if(days==0 and count==0):
                        result+=1
                    days+=1
                    if(days==7):
                        days=0
                    count+=1
                count=0
        years+=1

    return result

print(solution())