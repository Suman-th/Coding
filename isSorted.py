def isSorted(arr,n):

    inc = False
    dec = False
        
    for i in range(n-1):
           
        if arr[i] < arr[i+1]:
               
            inc = True
                
        if arr[i] > arr[i+1]:
                
            dec = True
            
        if inc and dec :
            return 0
        
    return 1


n = int(input())
arr = list(map(int, input().split()))
print(isSorted(arr,n))