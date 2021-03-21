N = int(input())
X = 0
x = []
for i in range(N):
    A, B = map(int, input().split())
    X -= A
    x.append(A + A + B)
x.sort()
ans = 0
while X <= 0:
    X += x.pop()
    ans += 1
print(ans)