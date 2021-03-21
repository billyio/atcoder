import itertools

N, K = map(int, input().split())
T = [list(map(int, input().split())) for n in range(N)]
town = [i for i in range(2,N+1)]
count = 0

for v in itertools.permutations(town):
    v = [1] + list(v) + [1]
    time = 0
    for i in range(len(v)-1):
        time += T[v[i]-1][v[i+1]-1]
    if time == K:
        count += 1

print(count)