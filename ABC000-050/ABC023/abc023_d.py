# just read and understand the code

from sys import stdin
input = stdin.buffer.readline
 
from itertools import accumulate
 
def main():
    n = int(input())
    hs = [tuple(map(int, input().split())) for _ in range(n)]
 
    # binary search
    left = max(hs, key=lambda x: x[0])[0]
    hs_right = max(hs, key=lambda x: x[0]+x[1]*(n-1))
    right = hs_right[0] + hs_right[1]*(n-1)

    while left < right:
        center = (left + right) // 2
 
        # cumulative sum
        cs = [0] * (n+1)
        for h, s in hs:
            cs[min(n, (center-h)//s)] += 1
        cs = list(accumulate(cs))
 
        for i, x in enumerate(cs[:n]):
            if i + 1 < x:
                left = center + 1
                break
        else:
            right = center
 
    print(left)
 
main()