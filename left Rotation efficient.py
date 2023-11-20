def Rotate(A,D,N):
    d= D%N
        
    g = gcd(D,N)
    k=0
        
    for i in range(g):
            
        temp = A[i]
            
        j=i
        while 1:
            k = (j + d)%N
            if k== i:
                break
                 
            A[j]=A[k]
            j = k
        A[j]=temp
    return A

def gcd(x,y):
    if x==0:
        return y
    else:
        return gcd(y%x,x)  

n, d = map(int, input().split())
A = list(map(int, input().split()))
print(Rotate(A,d,n))
