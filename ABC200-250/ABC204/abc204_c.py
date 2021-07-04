# Wrong 
# N, M = map(int, input().split())
# AB = []
# rode = [[i+1] for i in range(N)]
# for i in range(M):
#     a, b = map(int, input().split())
#     AB.append([a, b])

# for i in range(M):
#     a, b = AB[i]
#     for j in range(N):
#         if a in rode[j] and b not in rode[j]:
#             rode[j].append(b)
            
# print(rode)
# ans = 0
# for i in range(len(rode)):
#     ans += len(rode[i])

# print(ans)

# おまじない
import sys
sys.setrecursionlimit(10000)


N,M=map(int,input().split())
G=[[] for i in range(N)]
# G[i] は都市iから道路で直接繋がっている都市のリスト
for i in range(M):
    A,B=map(int,input().split())
    G[A-1].append(B-1)

print(G)

# dfs
def dfs(v):
    print(v, temp)
    if temp[v]: return  # 同じ頂点を2度以上調べないためのreturn
    temp[v]=True
    for vv in G[v]:
        dfs(vv)

ans=0

# 都市iからスタートする場合
for i in range(N):
    print(i)
    temp=[False]*N
    # temp[j] は都市jに到達可能かどうかを表す
    dfs(i)
    ans+=sum(temp)

print(ans)
