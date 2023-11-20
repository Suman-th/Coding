def power(a,n):
    
    res=1

    while n>0:
        if (n&1): # optimisation n&1 (binary exprsiion check) => n%2 !=0
            res= res*a
        a=a*a 
        n=n>>1 # binary optimistnsi n>>1 => n=n//2
    return res


a=3
n=20
print(power(a,n))