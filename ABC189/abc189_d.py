# wc
# N = int(input())
# OR = 0
# for i in range(N):
#     tmp = input()
#     if tmp == "OR":
#         OR += 1

# import math 
# def combinations_count(n, r):
#     return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

# c = combinations_count(N+1, OR+1)
# print(2**(N+1) - c)

# https://atcoder.jp/contests/abc189/editorial/537
# 例1
N = int(input())
S = list(input() for i in range(N))
 
dp = [[0, 0] for j in range(N+1)]

dp[0][0] = 1
dp[0][1] = 1
 
for i in range(1,N+1):
    if S[i-1] == "AND":
        dp[i][0] = dp[i-1][0]
        dp[i][1] = dp[i-1][0] + dp[i-1][1] *2
 
    elif S[i-1] == "OR":
        dp[i][0] = dp[i-1][0] * 2 + dp[i-1][1]
        dp[i][1] = dp[i-1][1]

print(dp[N][0])

# 例2
ans=1 #True False
for i in range(int(input())):
    if input()=='OR':
        ans += 2 << i
print(ans)