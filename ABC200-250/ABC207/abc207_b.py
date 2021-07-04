a, b, c, d = map(int,input().split())
for i in range(10**6):
    if a + b*i <= c*i*d:
        print(i)
        break
else:
    print(-1)