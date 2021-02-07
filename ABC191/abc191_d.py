# 未回答
# https://atcoder.jp/contests/abc191/submissions/20019868
# scale = 10**4
# X, Y, R = map(lambda x: round(float(x)*scale), input().split())
# r2 = R**2
# low = (Y-R + scale - 1) // scale # round up
# hi = (Y+R) // scale # round down
# ans = 0
# for y in range(low, hi+1):
#     dx2 = r2 - (Y - y*scale)**2
#     dx = int(dx2**0.5) + 1
#     while  dx**2 > dx2: dx -= 1
#     L = (X - dx + scale - 1) // scale
#     R = (X + dx) // scale
#     ans += R-L+1
# print(ans)


# https://atcoder.jp/contests/abc191/submissions/20020413
# decimal: 正確に丸められた十進浮動小数点算術をサポート

from decimal import Decimal
from math import ceil, floor
 
X, Y, R = map(Decimal, input().split())
 
left, right = ceil(X - R), floor(X + R)
 
ans = 0
for i in range(left, right + 1):
    d = (R**2 - (X - i)**2).sqrt()
    down, up = ceil(Y - d), floor(Y + d)
    ans += up - down + 1
 
print(ans)