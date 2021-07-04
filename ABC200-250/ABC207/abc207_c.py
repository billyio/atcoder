n = int(input())
line = []
for i in range(n):
    t, l, r = map(int,input().split())
    if t == 2:
        r -= 0.1
    elif t == 3:
        l += 0.1
    elif t == 4:
        l += 0.1
        r -= 0.1
    line.append([l, r])

ans = 0
for i in range(n):
    for j in range(i+1,n):
        # print(i, j, line[i], line[j])
        if line[j][0] - line[i][1] > 0 or line[i][0] - line[j][1] > 0:
            continue
        ans += 1
print(ans)
