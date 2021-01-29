# https://atcoder.jp/contests/abc076/tasks/abc076_b

N = int(input())
K = int(input())
start = 1
for i in range(N):
    start = min(start*2,start+K)
print(start)