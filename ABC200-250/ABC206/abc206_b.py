import math
n = int(input())
ans = math.sqrt(n * 2)
if (math.floor(ans) + 1) * math.floor(ans) / 2 >= n:
    print(math.floor(ans))
else:
    print(math.ceil(ans))