def Highest2nd(arr,n):

    first = secnd = float('-inf')

    for e in arr:
        if e>first:
            secnd = first
            first = e
        elif e<first and e>secnd:
            secnd = e
    
    if secnd == float('-inf'):
        return -1 
    return secnd

n = int(input())
arr = list(map(int, input().split()))
print(Highest2nd(arr,n))