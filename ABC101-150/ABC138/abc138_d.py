# よくわかっていない

# N, Q = map(int, input().split())
# graph = [[] for i in range(N+1)]
# for i in range(N-1):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# P = [0]*(N+1)
# for i in range(1, Q+1):
#     p, x = map(int, input().split())
#     P[p] += x

# C = [0]*(N+1)

# def dfs(v):
#     visited = {v}
#     C[v] = P[v]
#     stack = [v]
#     while stack:
#         now_v = stack[-1]
#         if graph[now_v]:
#             w = graph[now_v].pop()
#             if w not in visited:
#                 visited.add(w)
#                 stack.append(w)
#                 C[w] += P[w]
#                 C[w] += C[now_v]
#         else:
#             stack.pop()
#     return C


# ans = dfs(1)[1:]
# print(*ans, sep=" ")

N, Q = map(int, input().split())
G = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

P = [0] * (N+1)

for _ in range(Q):
    p, x = map(int, input().split())
    P[p] += x

# print(G)
# print(P)

def dfs(v, p):
    for c in G[v]:
        if c == p:
            continue
        P[c] += P[v]
        dfs(c, v)

dfs(1,-1)

print(*P[1:])