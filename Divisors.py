def divisors(n):
    i=1
    while i*i<n:
        if n%i==0:
            print(i,end=" ")
        i+=1
        
    if i*i!=n:
        i=i-1

    while i>=1:
        if n%i==0:
            print(int(n/i),end=" ")
        i-=1
n=84
divisors(n)