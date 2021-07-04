from heapq import heappop, heappush, heapify
import collections

def dijkstra(start, graph): # (始点, グラフのリスト)
    INF = 10 ** 18
    dist = [INF] * n 
    check = [False] * n
    dist[start] = 0
    q = [(0, start)] # （距離・ノード）
    while q:
        v = heappop(q)[1] # 今いるノード
        if check[v]: continue
        check[v] = True # 訪問済み
        for i, j in graph[v]: # 先のノード・距離
            if check[i] != False: continue
            if dist[i] <= dist[v] + j: continue
            dist[i] = dist[v] + j
            heappush(q, (dist[i], i)) # 必ず[0]が距離になるように（優先度付きキュー）
    return dist

n, m = map(int,input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a, b, c = map(int,input().split())
    g[a - 1].append((b - 1, c))
    g[b - 1].append((a - 1, c))

x = dijkstra(0, g)
y = dijkstra(n - 1, g)

for i in range(n):
    ans = x[i] + y[i]
    print(ans)