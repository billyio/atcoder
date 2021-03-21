N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
XY.sort()
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if (XY[i][1]-XY[j][1]) * (XY[i][0]-XY[k][0]) == (XY[i][1]-XY[k][1]) * (XY[i][0]-XY[j][0]):
                print("Yes")
                exit()
print("No")