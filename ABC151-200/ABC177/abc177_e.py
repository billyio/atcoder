import functools

def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a%b)

def gcd(nums):
    return functools.reduce(euclid, nums)

def prime_decomposition(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n /= i
            table.append(i)
            i += 1
    if n > 1:
        table.append(n)
    return table

N = int(input())
A = list(map(int, input().split()))

print(prime_decomposition(A[0]))
print(prime_decomposition(A[1]))
print(prime_decomposition(A[2]))

# if 

#     print("pairwise coprime")
# elif gcd(A) == 1:
#     print("setwise coprime")
# else:
#     print("not coprime")