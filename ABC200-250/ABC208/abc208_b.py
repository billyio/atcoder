import math
p = int(input())
coin = [math.factorial(x) for x in reversed(range(1,11))]

ans = 0
for i in range(10):
    q, p = p // coin[i], p % coin[i]
    ans += q

print(ans)