from heapq import heappush, heappop

def dijkstra(start, graph):
    INF = 10 ** 18
    check = [False] * n
    dist = [INF] * n
    dist[start] = 0
    q = [(dist[start], start)]
    while q:
        node = heappop(q)[1]
        if check[node]: continue
        check[node] = True
        for i in graph[node]:
            if check[i]: continue
            if dist[i] < dist[node]: continue
            dist[i] = dist[node] + 1
            heappush(q, [dist[i], i])
    return dist

n = int(input())
graph = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int,input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

zero_dist = dijkstra(0, graph)
max_dist = max(zero_dist)
max_index = zero_dist.index(max_dist)
ans = dijkstra(max_index, graph)
print(max(ans) + 1)