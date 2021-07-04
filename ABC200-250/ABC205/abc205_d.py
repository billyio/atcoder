# 自作二分探索より標準ライブラリだとうまくいった
import itertools, bisect

n, q = map(int, input().split())
a = [0] + list(map(int, input().split()))
a_ = [0]
for i in range(n):
    a_.append(a[i+1] - a[i] - 1)
a_ = list(itertools.accumulate(a_))
# print(a)
# print(a_)

for i in range(q):
    k = int(input())
    if a_[-1] < k:
        print(a[-1] + k - a_[-1])
    else:
        left = bisect.bisect_left(a_, k)
        print(a[left] - 1 - a_[left] + k)
