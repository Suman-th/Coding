import math
def roots(a,b,c):

    sq= b*b-4*a*c
    print(sq)
    if sq<0:
        return [-1]
    
    x= math.floor(0.5*(-b+math.sqrt(sq))/a)
    y= math.floor(0.5*(-b-math.sqrt(sq))/a)
    print(x,y)
    
    if b*a>=0:
        return [y,x]
    else:
        return [x,y]
    
a=-264 
b=-750 
c=504
print(roots(a,b,c))