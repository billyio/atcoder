N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
tmp = 10**5*2
for i in range(N):
    for j in range(N):
        if i != j:
            tmp = min(tmp, max(AB[i][0],AB[j][1]))
        else:
            tmp = min(tmp, AB[i][0]+AB[i][1])
print(tmp)