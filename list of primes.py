def listofprime(n):
    l=[]
    prime=[True for i in range(n+1)] #boolean array
    p=2 
    while (p*p <=n) :
        if prime[p]==True:

            # Updating all multiple of p
            for i in range(p*p,n+1, p):
                prime[i]=False
        p+=1
    for p in range(2,n+1):
        if prime[p]:
            l.append(p)
    return l

n= 64
print(listofprime(n))

