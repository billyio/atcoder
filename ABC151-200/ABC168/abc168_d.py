# https://note.com/melon_ms_mtcc/n/nd2c0c7c16edb

# from collections import deque

# n, m = map(int, input().split())

# graph = [[] for _ in range(n+1)]

# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)


# dist = [-1] * (n+1)
# dist[0] = 0
# dist[1] = 0

# d = deque()
# d.append(1)

# while d:
#     v = d.popleft()
#     for i in graph[v]:
#         if dist[i] != -1:
#             continue
#         dist[i] = dist[v] + 1
#         d.append(i)

# ans = dist[2:]
# print(*ans, sep="\n")


from collections import deque
N,M = map(int, input().split())
neighbor = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int, input().split())
    neighbor[a].append(b)
    neighbor[b].append(a)

mark = [-1]*(N+1)
q = deque()
q.append(1)
mark[1] = 0

while q:
    print(q, neighbor)
    at = q.popleft()
    for to in neighbor[at]:
        if mark[to] != -1:
            continue
        mark[to] = at
        q.append(to)

print('Yes')
for l in mark[2:]:
    print(l)