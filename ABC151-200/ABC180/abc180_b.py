N = int(input())

total = 0
for i in range(N):
    A, B = map(int, input().split())
    total +=  (A+B) * (B-A+1) / 2

print(int(total))
