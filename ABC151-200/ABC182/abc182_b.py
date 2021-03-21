# AC 約数列挙しその約数をもつ最も多い数を出力
def divisor(n): 
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table

import collections

N = int(input())
A = list(map(int, input().split()))

B = [divisor(a) for a in A]
C = [i for i in sum(B, []) if i != 1]
D = collections.Counter(C)

print(D.most_common()[0][0])

# 公式解説　max1000と少ないから全列挙
N = int(input())
A = list(map(int, input().split()))
 
ans = -1
mx = 0
 
for x in range(2, 1001):
	s = sum(a % x == 0 for a in A)
	if mx < s:
		mx = s
		ans = x
 
print(ans)