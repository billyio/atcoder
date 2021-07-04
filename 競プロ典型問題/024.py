n, k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

dif = 0
for i in range(n):
    dif += abs(a[i] - b[i])

if (k % 2 == 0) == (dif % 2 == 0) and dif <= k:
    print("Yes")
else:
    print("No")