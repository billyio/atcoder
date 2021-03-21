# import itertools

# N, M = map(int, input().split())
# xy =[list(map(int, input().split())) for _ in range(M)]

# G = [[0] * N for _ in range(N)]
# for i in range(M):
#     xi, yi = xy[i][0], xy[i][1]
#     G[xi-1][yi-1] = 1
#     G[yi-1][xi-1] = 1

# # print(G)
# mx = 0
# for bits in itertools.product([0, 1], repeat=N):
#     group = []
 
#     for i in range(N):
#         if bits[i] == 1:
#             group.append(i)
    
#     for x, y in itertools.combinations(group, 2):
#         if G[x][y] == 0:
#             break
#     else:
#         mx = max(len(group), mx)

# print(mx)

# 二分探索
# https://tawara.hatenablog.com/entry/2015/05/15/020817
from itertools import combinations as comb

def k_clique_solve(relation, max_members, k):
    for members in comb(max_members,k):
        for r in comb(members,2):
            if r in relation:
                continue
            break
        else:
            return True
    else:
        return False

N, M = map(int, input().split())
max_members = range(N)

relation = set()

for i in range(M):
    x, y = map(int, input().split())
    relation.add((x-1,y-1))
 
left = 1
right = N + 1
while right - left > 1:
    mid = (left + right) // 2
    if k_clique_solve(relation, max_members, mid):
        left = mid
    else:
        right = mid
print(left)