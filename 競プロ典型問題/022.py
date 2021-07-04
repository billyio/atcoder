a, b, c = map(int,input().split())
import functools
def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a%b)

def gcd(nums):
    return functools.reduce(euclid, nums)

gcd = gcd([a, b, c])
ans = (a-1) // gcd + (b-1) // gcd + (c-1) // gcd
print(ans)