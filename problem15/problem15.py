import math

def solution(n):
    return (math.factorial(2*n))/pow(math.factorial(n),2)

print(solution(20))