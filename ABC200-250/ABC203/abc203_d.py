N, K = map(int, input().split())

A = []
for i in range(N):
    Aij = list(map(int, input().split()))
    A.append(Aij)

ponds = []

for i in range(N-K+1):
    for j in range(N-K+1):
        pond = []
        for k1 in range(K):
            for k2 in range(K):
                pond.append(A[i+k1][j+k2])
        l, r = -1, 10 ** 9
        while r - l > 1:
            m = (l + r) // 2
            if med <  
        ponds.append(pond)

print(ponds)