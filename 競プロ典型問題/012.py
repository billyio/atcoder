from collections import defaultdict

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

H, W = map(int, input().split())
Q = int(input())
grid = [[False] * (W+2)] * (H+2)
uf = UnionFind(H*W+2)
around = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(Q):
    q = list(map(int, input().split()))
    print(uf.parents)
    if q[0] == 1:
        grid[q[1]][q[2]] = True
        for dy, dx in around:
            if grid[q[1] + dy][q[2] + dx]:
                uf.union((q[1]-1)*W+q[2], (q[1]+dy-1)*W+q[2]+dx)
    else:
        grid[q[1]][q[2]] = True
        grid[q[3]][q[4]] = True
        if uf.same((q[1]-1)*W+q[2], (q[3]-1)*W+q[4]) and grid[q[1]][q[2]] and grid[q[3]][q[4]]:
            print("Yes")
        else:
            print("No")