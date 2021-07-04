N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))
A.append(L)


dif = [A[0]]
for i in range(N):
    dif.append(A[i+1] - A[i])

def can_split(x):
    length = 0
    cnt = 0
    for i in dif:
        length += i
        if length >= x:
            length = 0
            cnt += 1
    return cnt

def bisect(ng, ok):
    while ng - ok > 1:
        mid = (ng + ok) // 2
        if can_split(mid) >= K + 1:
            ok = mid
        else:
            ng = mid
    return ok

print(bisect(L+1, -1))