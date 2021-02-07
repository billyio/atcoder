# https://atcoder.jp/contests/abc191/submissions/20021327
from heapq import heappop, heappush

INF = 10**20

N, M = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    g[a - 1].append((b - 1, c))
print(g)

for s in range(0, N):
    dist = [-1] * len(g)
    que = [(0, s)]
    while len(que):
        pd, pn = heappop(que)
        if dist[pn] != -1:
            continue
        if pd != 0:
            if pn == s:
                print(pd)
                break
            dist[pn] = pd
        # g[pn]に隣接する点とコストをキューに追加
        for cn, d in g[pn]:
            if dist[cn] != -1:
                continue
            cd = pd + d
            heappush(que, (cd, cn))
    else:
        print(-1)