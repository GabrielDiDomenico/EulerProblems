import math

def solution():
    nums = [0,1,2,3,4,5,6,7,8,9]
    i=0
    aux=0
    j=0
    while(i<1000000):
        while(j<9):
            aux=nums[j]
            nums[j]=nums[j+1]
            nums[j+1]=aux
            j+=1
            i+=1
            print nums
        j=0

    return nums

print solution()
        
        