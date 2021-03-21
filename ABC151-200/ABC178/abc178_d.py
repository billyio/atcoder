# https://drken1215.hatenablog.com/entry/2020/10/11/211000
N = int(input())

if N == 1:
    print(0)
    exit()

dp = [0 for _ in range(N+1)]
dp[0], dp[1], dp[2] = 1, 0, 0
for i in range(2,N+1):
    for j in range(0,i-2):
        dp[i] += dp[j]

print(dp[-1] % (10**9+7))