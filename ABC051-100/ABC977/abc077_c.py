N = int(input())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))
C = sorted(map(int, input().split()))

A_ind = 0
C_ind = 0
ans = 0
for B in B:
    while A_ind < N and A[A_ind] < B:
        A_ind += 1
    while C_ind < N and C[C_ind] <= B:
        C_ind += 1
    ans += A_ind * (N - C_ind)

print(ans)


import bisect
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
B.sort()
C.sort()
cnt = 0
for b in B:
  n1 = bisect.bisect_left(A, b)
  n2 = N - bisect.bisect_right(C, b)
  cnt += n1 * n2
print(cnt)