N = int(input())
A = list(map(int, input().split()))

res = 0
Asummx = 0
tmp = 0
Asum = 0 

for i in A:
    Asum += i
    Asummx = max(Asummx, Asum)
    res = max(res, tmp+Asummx)
    tmp += Asum

print(res)