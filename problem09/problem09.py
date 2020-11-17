def solution():
    a=200
    b=201
    c=202
    aux=0
    limit=500
    while(a<limit):
        aux=a+b+c
        if(aux==1000):
            if((pow(a,2)+pow(b,2)==pow(c,2))):
                return(a*b*c)
        if(c<limit):
            c+=1
        elif (b<limit):
            c=202
            b+=1
        else:
            b=201+(a-201)
            c=202+(b-202)
            a+=1

print(solution())