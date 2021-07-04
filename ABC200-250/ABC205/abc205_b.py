n = int(input())
a = list(map(int, input().split()))
a.sort()
for i in range(n):
    if i+1 != a[i]:
        print("No")
        break
else:
    print("Yes")
