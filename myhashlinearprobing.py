def insert(a,k,h,n):
    i= k%n
    if h[i]==-1:
        h[i] = a
    else: insert(a,i+1,h,n)


    
def linearProbing(hashSize, arr, sizeOfArray):
    #Your code here
    n = hashSize
    m = sizeOfArray
    load_cap = n/m
        
    h = [-1]*n
        
    for a in arr:
        temp = a%n
        insert(a,temp,h,n)

    return h


hashSize=10
sizeOfArray=4
arr= [4, 14, 24, 44]
h= linearProbing(hashSize, arr, sizeOfArray)
for i in h:
    print(i,end=" ")