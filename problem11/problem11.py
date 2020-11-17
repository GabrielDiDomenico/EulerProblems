def makeMatrix():
    
    arq = open('p11matrix.txt', 'r')
    text = []  
    text = arq.readlines()
    matrix=[]


    arq.close()

    for x in text:
        matrix.append(x.split())

   
    j=0
    for i in matrix:
        while(j<20):
            i[j]=int(i[j])
            j+=1
        j=0

        
    return matrix

def makeProducts(i,j):
    grid = makeMatrix()

    array=[]
    array.append(grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j])
    array.append(grid[i][j]*grid[i-1][j]*grid[i-2][j]*grid[i-3][j])
    array.append(grid[i][j]*grid[i][j-1]*grid[i][j-2]*grid[i][j-3])
    array.append(grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3])
    array.append(grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3])
    array.append(grid[i][j]*grid[i-1][j-1]*grid[i-2][j-2]*grid[i-3][j-3])
    array.append(grid[i][j]*grid[i-1][j+1]*grid[i-2][j+2]*grid[i-3][j+3])
    array.append(grid[i][j]*grid[i+1][j-1]*grid[i+2][j-2]*grid[i+3][j-3])
    
    return(max(array))
    
    

def solution():
    sol=1
    aux=1
    for i in range(20):
        if(i>2 and i<17):
            for j in range(20):
                if(j>2 and j<17):
                    aux = makeProducts(i,j)
                    if(aux>sol):
                        sol=aux
    return sol


print(solution())
