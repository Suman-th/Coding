# count trailing 0s
# in n !

# Function to return
# trailing 0s in
# factorial of n
def findTrailingZeros(n):
    
    # Initialize result
    count=0
    i=5
    #Trailing 0s in n! = Count of 5s in prime factors of n! = floor(n/5) + floor(n/25) + floor(n/125) + ....
    while (n/i>1):
        count+= n//i # Keep dividing n by
        i*=5 # powers of 5 and

    return(count)
n = int(input())
print("Count of trailing 0s "+"in 100 ! is", findTrailingZeros(n))