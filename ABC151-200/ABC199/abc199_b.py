N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

count = min(B) - max(A) + 1
if count > 0:
    print(count)
else:
    print(0)