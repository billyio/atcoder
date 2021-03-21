import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
 
N = int(input())
print(combinations_count(N-1,11))