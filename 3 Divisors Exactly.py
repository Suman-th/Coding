def isPrime(n):

    if n <= 1:
        return False
    if n <= 3:
        return True
    if n%2 == 0 or n%3==0:
        return False
    
    i=5
    while (i*i<=n) :
        if n % i == 0  or n%(i+2) == 0:
            return False
        i+=6
    
    return True

def divisor3(n):
    
    k=0
    i=2
    while i*i<=n :

        if isPrime(i):
            k+=1
        i+=1
    return k

N = 49
print(divisor3(N))
    