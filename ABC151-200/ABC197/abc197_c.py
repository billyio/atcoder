# bit全探索

N = int(input())
A = list(map(int, input().split()))

ans = float("inf")
for i in range(2 ** (N-1)):
    a = A[0]
    b = 0
    for j in range(N-1):
        if i >> j & 1:
            b ^= a
            a = A[j+1]
        else:
            a |= A[j+1]
    b ^= a
    ans = min(ans, b)
print(ans)