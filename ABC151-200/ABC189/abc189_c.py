# wc
# N = int(input())
# A = list(map(int,input().split()))

# ans = 0
# b = list(set(A))
# b.sort()

# from itertools import groupby

# for i in range(len(b)):
#     max_count = [sum(item) for val, item in groupby([1 if x >= b[i] else -1 for x in A])]
#     tmp = b[i] * max(max_count)
#     ans = max(ans, tmp)
# print(ans)


# ans = 0
# b = list(set(A))
# b.sort()

# for i in range(len(b)):
#     tmp = 0
#     for j in range(N):
#         if A[j] >= b[i]:
#             tmp += b[i]
#             ans = max(ans, tmp)
#         else:
#             tmp = 0

# print(ans)

# 素直に全探索
N = int(input())
A = list(map(int, input().split()))
INF = 10 ** 9
ans = 0
for i in range(N):
    for j in range(N):
        m = min(A[i], A[j])
        ans = max(ans, m * (j - i + 1))
print(ans)