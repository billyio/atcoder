# WA
# N, W = map(int, input().split())

# STP = []
# for i in range(N):
#     s, t, p = map(int, input().split())
#     STP.append([s, t-1, p])

# r = {}
# for s,t,p in STP:
#     if s in r:
#         r[s] = r[s] + p 
#     elif s not in r:
#         r[s] = p
#     if t in r and t-s >= 1:
#         r[t] = r[t] + p
#     elif t not in r:
#         r[t] = p
#     # print(r)

# for v in r.values():
#     if v > W:
#         print("No")
#         break
# else:
#     print("Yes")

# いもす法
import itertools
 
N, W = map(int, input().split())
STP = [list(map(int, input().split())) for _ in range(N)]
 
item_num = max([i[1] for i in STP])
An = [0] * (item_num + 2)
 
for s, t, p in STP:
    An[s] += p
    An[t] -= p
print(An)
Bn = list(itertools.accumulate(An))
print(Bn)
if max(Bn) > W:
    print('No')
else:
    print('Yes')