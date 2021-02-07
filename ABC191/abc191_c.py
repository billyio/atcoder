# 未回答

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
ans = 0
for h in range(H-1):
    for w in range(W-1):
        arr = [S[h][w], S[h+1][w], S[h][w+1], S[h+1][w+1]]
        cnt = arr.count('#')
        if cnt % 2: 
            ans += 1
print(ans)