# AC
N, S, D = map(int, input().split())

ans = 0
for i in range(N):
    x, y = map(int, input().split())
    if x < S and y > D:
        ans += y

if ans == 0:
    print("No")
else:
    print("Yes")