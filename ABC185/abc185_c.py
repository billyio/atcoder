import math
def ncr(n,r):
    return(math.factorial(n)//(math.factorial(r)*math.factorial(n-r)))
 
n = int(input())
print(ncr(n-1,11))