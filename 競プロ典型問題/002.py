N = int(input())

ans = []

for i in range(2 ** (N)):
    cnt = 0
    brackets = ""

    # 0: ), 1:( とする
    for j in range(N):
        if i >> j & 1:
            brackets += "("
            cnt += 1
        else:
            brackets += ")"
            cnt -= 1
        
        if cnt < 0:
            break
        if j == N-1 and cnt == 0:
            ans.append(brackets)
        
ans.sort()
for brackets in ans:
    print(brackets)
        


