import math
t = int(input())
l, x, y = map(int, input().split())
q = int(input())
for i in range(q):
    e = int(input())
    th = e/t*360
    rad = math.radians(th)
    x_, y_, z_ = 0, -l / 2 * math.sin(rad), l / 2  - l / 2 * math.cos(rad)
    dist = math.sqrt((x_ - x)**2 + (y_ - y)**2 + (z_ - 0)**2)
    ans = math.degrees(math.asin(z_ / dist))
    print(ans)