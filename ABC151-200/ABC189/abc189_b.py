# wc
# N, X = map(int, input().split())
# vp = []
# for i in range(N):
#     v, p = map(int, input().split())
#     vp.append([v,p])

# drunk = 0
# for j in range(N):
#     v, p = vp[j][0], vp[j][1]
#     drunk += v * p / 100
#     print(j, drunk)
#     if drunk > X:
#         print(j+1)
#         break
# else:
#     print(-1)

# 浮動小数点の問題を回避する
N,X = map(int,input().split())
s = 0
for i in range(N):
  v,p = map(int,input().split())
  s += v*p
  if s > X*100:
    print(i+1)
    break
else:
    print(-1)