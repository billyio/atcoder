K = int(input())
S = input()[:4]
T = input()[:4]
cnt = [K] * 10
for c in S:
    cnt[int(c)] -= 1
for c in T:
    cnt[int(c)] -= 1

print(cnt)

def score(S):
    cnt = [0] * 10
    for c in S:
        cnt[int(c)] += 1
    ans = 0
    for i in range(1, 10):
        ans += i * 10 ** cnt[i]
    return ans

ans = 0

for i in range(1, 10):
    if cnt[i] == 0:
        continue
    for j in range(1, 10):
        if i == j or cnt[j] == 0:
            continue
        if score(S + str(i)) > score(T + str(j)):
            ans += cnt[i] * cnt[j]

for i in range(1, 10):
    if cnt[i] < 2:
        continue
    if score(S + str(i)) > score(T + str(i)):
        ans += cnt[i] * (cnt[i] - 1)

N = 9 * K - 8
print(ans / N / (N - 1))


# import collections

# K = int(input())
# S = int(input()[:-1])
# T = int(input()[:-1])

# # s_count = collections.Counter(list(str(S)))
# # t_count = collections.Counter(list(str(T)))
# s_list = []
# t_list = []

# s_score_list = []
# t_score_list = []

# s_dist = 9
# for i in range(1,10):
#     tmp = collections.Counter(list(str(S)))
#     if tmp[str(i)] >= K:
#         s_dist -= 1
#         continue
#     elif str(i) in tmp:
#         tmp[str(i)] = tmp[str(i)] + 1
#     else:
#         tmp[str(i)] = 1
#     s_list.append(tmp)

# t_dist = 9
# for i in range(1,10):
#     tmp = collections.Counter(list(str(T)))
#     if tmp[str(i)] >= K:
#         t_dist -= 1
#         continue
#     elif str(i) in tmp:
#         tmp[str(i)] = tmp[str(i)] + 1
#     else:
#         tmp[str(i)] = 1
#     t_list.append(tmp)

# for s_count in s_list:
#     print(s_count)
#     tmp_score = 0
#     for i in range(1,10):
#         if str(i) in s_count:
#             tmp_score += i * (10 ** s_count[str(i)])
#             print(i, s_count[str(i)], tmp_score)
#         else:
#             tmp_score += i
#     s_score_list.append(tmp_score)

# for t_count in t_list:
#     print(t_count)
#     tmp_score = 0
#     for i in range(1,10):
#         if str(i) in t_count:
#             tmp_score += i * (10 ** t_count[str(i)])
#             print(i, t_count[str(i)], tmp_score)
#         else:
#             tmp_score += i
#     t_score_list.append(tmp_score)

# print(s_score_list)
# print(t_score_list)

# win = 0
# for s in s_score_list:
#     for t in t_score_list:
#         if s > t:
#             print(s,t)
#             win += 1

# print(s_dist, t_dist, s_dist*t_dist)
# print(win)