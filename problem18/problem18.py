def makeTri():
    
    arq = open('p18tri.txt', 'r')
    text = []  
    text = arq.readlines()
    tri=[]


    arq.close()

    for x in text:
        tri.append(x.split())

    for i in tri:
        if(len(i)<100):
            while(len(i)<100):
                i.append(0)
    j=0
    for i in tri:
        while(j<100):
            i[j]=int(i[j])
            j+=1
        j=0

        
    return tri



def solution(tri, m, n): 

    for i in range(m-1, -1, -1): 
        for j in range(i+1): 
            if (tri[i+1][j] > tri[i+1][j+1]): 
                tri[i][j] += tri[i+1][j] 
            else: 
                tri[i][j] += tri[i+1][j+1] 

    return tri[0][0] 



print(solution(makeTri(),14,14))