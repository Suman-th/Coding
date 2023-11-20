def Rotate(A,d,n):

    d= D%N
        
    temp = A[:d]
    del A[:d]
        
    A.extend(temp)
        
    return A



n = int(input())
d = int(input())
A = list(map(int, input().split()))
print(Rotate(A,d,n))