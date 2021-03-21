# RE
# from itertools import combinations

# N = int(input())
# A = list(map(int, input().split()))

# sub = []
# add = 0
# for v in combinations(A, 2):
#     add += (list(v)[1]-list(v)[0]) ** 2

# print(add)

# from itertools import combinations
# N = int(input())
# A = list(map(int, input().split()))
# rss = [i**2 for i in range(201)]

# add = 0
# for v in combinations(A, 2):
#     add += rss[abs(list(v)[1]-list(v)[0])]

# print(add)

N = int(input())
A = list(map(int, input().split()))

Sum = 0

cnt = [0] * 401
for i in A:
    cnt[i+200] += 1

print(cnt)

for i in range(1, 401):
    for j in range(0, i):
        Sum += cnt[i]*cnt[j]*(i-j)**2
    
print(Sum)

