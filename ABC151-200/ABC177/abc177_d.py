from collections import defaultdict

# 参考：　https://note.nkmk.me/python-union-find/
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
AB = [list(map(int, input().split())) for _ in range(M)]
uf = UnionFind(N)

for A, B in AB:
    if not uf.same(A, B):
        A -= 1
        B -= 1
        uf.union(A, B)

print(max([abs(i) for i in uf.parents if i < 0]))