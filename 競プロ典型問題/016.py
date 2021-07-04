n = int(input())
a, b, c = map(int, input().split())
abc = sorted([a,b,c])
cnt = 10**9
for i in reversed(range(n//abc[2]+1)):
    for j in reversed(range((n-i*abc[2])//abc[1]+1)):
        k = n - i*abc[2] - j*abc[1]
        if k % abc[0] == 0 and k >= 0:
            cnt = min(cnt, i+j+k//abc[0])
print(cnt)