# AC
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

if r1 == r2 and c1 == c2:
    print(0)
elif r1+c1 == r2+c2 or r1-c1 == r2-c2 or abs(r1-r2) + abs(c1-c2) <= 3:
    print(1)
# 和差の偶奇が一致するなら2回で移動可能
elif (abs(r1+c1)%2 == 0 and abs(r2+c2)%2 == 0) or (abs(r1+c1)%2 == 1 and abs(r2+c2)%2 == 1):
    print(2)
# 斜め1回移動後, 距離3以内なら2回で移動可能
elif abs(abs(r1+c1) - abs(r2+c2)) <= 3 or abs(abs(r1-c1) - abs(r2-c2)) <= 3:
    print(2)
# 3マス以上6マス以内
elif 3 < abs(r1-c1) + abs(r2-c2) <= 6:
    print(2)
else:
    print(3)