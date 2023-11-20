def power(a,n):
    if n==0:
        return 1
    temp= power(a,n//2)
    temp= temp*temp
    if n%2==0:
        return temp
    else:
        return a*temp

a=3
n=10
print(power(a,n))