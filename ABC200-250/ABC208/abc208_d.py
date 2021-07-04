# 未完：ダイクストラ法しか頭になかった。他の最短経路手法知っててもできないと思うが

import sys

N, M = map(int, sys.stdin.buffer.readline().split())
ABC = []
for _ in range(M):
  a,b,c = map(int,input().split())
  ABC.append([a,b,c])

dp = [[1 << 60] * N for i in range(N)]
for i in range(N):
  dp[i][i] = 0
for a, b, c in ABC:
  dp[a - 1][b - 1] = c

# print(dp)

answer = 0
for k in range(N):
  nxt = [[0] * N for i in range(N)]
  for i in range(N):
    for j in range(N):
      nxt[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
      if nxt[i][j] < 1 << 59:
        answer += nxt[i][j]
  dp = nxt
print(answer)


