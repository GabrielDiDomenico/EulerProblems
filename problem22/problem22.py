def makeNames():
    arq = open('p22names.txt', 'r')
    text = ""  
    text = arq.readlines()
    names=""


    arq.close()

    names = text[0].split(",")
    i=0
    while(i<len(names)):
        names[i] = names[i].replace('"','')
        i+=1

    return names

def nameValue(name):
    alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    value=0
    for x in name:
        i=1
        while(alphabet[i-1]!=x):
            i+=1
        value+=i
    
    return value


def solution():
    i=1
    names=makeNames()
    names.sort()
    result=0
    while(i<len(names)+1):
        result+= i*nameValue(names[i-1])
        i+=1

    return result
        

print solution()