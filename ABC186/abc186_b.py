import itertools

H, W = map(int, input().split())

A = []
for i in range(H):
    A.append(map(int, input().split()))

A = list(itertools.chain.from_iterable(A))
mi = min(A)

print(sum(A) - mi*H*W)