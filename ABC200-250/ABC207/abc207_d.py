import math
import numpy as np

n = int(input())
s, t = [], []

for i in range(n):
    a, b = map(int,input().split())
    s.append([a, b])

for i in range(n):
    c, d = map(int,input().split())
    t.append([c, d])

s_ctr = sum(s) / n
t_ctr = sum(t) / n



print(s)
print(t)

s_angle = []
for i in range(n):
    m = s[i][0] - s_ctr_x
    n = s[i][1] - s_ctr_y
    s_angle 


import sys
input = sys.stdin.buffer.readline
inputs = sys.stdin.buffer.readlines
# 入力受け取りパート
N = int(input())
if N == 1:
    # 一個しかなければもちろんok,ここではねないと後のu = Sgp[0]で配列外参照に
    print('Yes')
    quit()

# 重心を整数成分にしたほうが誤差の影響が少ないのでN倍(Nは正なのでこれをやっても一致可能性に影響なし)
S = [N*complex(*map(int, input().split())) for i in range(N)]
T = [N*complex(*map(int, i.split())) for i in inputs()]

GofS = sum(S)/N
GofT = sum(T)/N
# 重心と一致する点が両方にあると縮約が起きて判定が出来なくなるので別途処理
Sgp = [p-GofS for p in S if p.real != GofS.real or p.imag != GofS.imag]
Tgp = [p-GofT for p in T if p.real != GofT.real or p.imag != GofT.imag]

if len(Sgp) != len(Tgp):
    # 片方にだけ重心と一致する点が存在した場合、もちろん一致不可
    print('No')
    quit()

u = Sgp[0]
eps = 10**-2
Ru = abs(u)
for v in Tgp:
    if abs(v) == Ru:
        rotate=u/v
        if all(any(abs(X*rotate-omega) < eps for omega in Sgp) for X in Tgp):
            print('Yes')
            quit()
# ワンライナーのほうが制御回りが楽かも
#print('Yes' if any(abs(v) == Ru and all(any(abs(X*u-omega*v) < eps for omega in Sgp) for X in Tgp)for v in Tgp) else "No")

print('No')
