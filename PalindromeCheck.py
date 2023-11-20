def Palindromecheck(n):

    rev=0
    temp=n
    while temp!=0:
        t=temp%10
        rev= rev*10+t
        temp=temp//10
    return(rev==n)
n=int(input())
if Palindromecheck(n):
    print("Yes")
else:
    print("No")
