N = int(input())
mi = 10**10
for i in range(N):
    a, p, x = map(int, input().split())
    if x > a and p < mi:
        mi = p

if mi != 10**10:
    print(mi)
else:
    print(-1)