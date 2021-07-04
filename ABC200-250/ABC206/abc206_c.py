import collections

n = int(input())
a = list(map(int, input().split()))

c = collections.Counter(a)
a_cnt = []
for i in range(n):
    a_cnt.append(c[a[i]] - 1)
    c[a[i]] -= 1

ans = n * (n-1) / 2 - sum(a_cnt)

print(int(ans))