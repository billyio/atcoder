# WC
# N = int(input())
# T = list(map(int, input().split()))

# T.sort(reverse=True)
# T.sort(reverse=True)
# a, b = 0, 0
# for i in range(len(T)):
#     if a + T[i] - b > b + T[i] - a:
#         b += T[i]
#     else:
#         a += T[i]

# print(T)
# print(max(a, b))

n = int(input())
t = list(map(int,input().split()))
q = sum(t)
s = q/2
dp = [[False]*(q+1) for _ in range(n+1)]
dp[0][0] = True
# print(dp[0])

for i in range(1,n+1):
    for j in range(q+1):
        if j - t[i-1] >= 0 and dp[i-1][j-t[i-1]]:
            dp[i][j] = True
        else:
            dp[i][j] = dp[i-1][j]

# print(*dp,sep="\n")
ans = float('inf')
for k in range(q):
    if dp[n][k]:
        ans = min(ans,abs(s-k))

print(int(ans+s))