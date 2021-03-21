N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

sumA = sum(A)
ans = 0
for i in range(N-1):
    sumA = sumA - A[i]
    ans += A[i]*(N-i-1) - sumA

print(ans)