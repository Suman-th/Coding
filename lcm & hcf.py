def GCD(x,y):
    if y==0:
        return x
    else:
        return GCD(y,x % y)
def LCM(x,y):
    return (x*y/GCD(x,y))

x,y= map(int, input().split())
print(GCD(x,y))
print(LCM(x,y))