# 解説読んだけど、dfsのところが分からない
# https://atcoder.jp/contests/abc199/submissions/22051931

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    
    def same(self, x, y):
        return self.find(x) == self.find(y)


N, M = map(int, input().split())
uf = UnionFind(N)
graph = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    uf.union(a,b)
    graph[a].append(b)
    graph[b].append(a)

colors = [-1]*N

print(graph)
print(colors)
print("uf parents",uf.parents)

def dfs(k, order):
    if k == len(order): return 1
    i = order[k]
    cnt = [0] * 3
    for j in graph[i]:
        if colors[j] >= 0:
            cnt[colors[j]] += 1
    r = 0
    for c in (0, 1, 2):
        if cnt[c]: continue
        colors[i] = c
        r += dfs(k+1, order)
        colors[i] = -1
    return r

visited = [0] * N
def dfs_order(i, order):
    print(i, order)
    if visited[i]: return
    visited[i] = 1
    order.append(i)
    for j in graph[i]:
        if visited[j]: continue
        dfs_order(j, order)
    return

ans = 1
for i in [i for i in range(N) if uf.parents[i] < 0]:
    print(i)
    order = []
    dfs_order(i, order)
    ans *= dfs(0, order)
print(ans)