import math
def primefactors(n):
    
    while n%2==0:
        print(2, end= " ")
        n = n/2
    
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i==0 :
            print(i, end=" ")
            n=n/i
    if n>2:
        print(int(n))

n= 315
primefactors(n)