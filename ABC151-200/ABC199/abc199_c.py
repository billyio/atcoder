N = int(input())
S = list(input())
Q = int(input())

flip = False
for _ in range(Q):
    T, A, B = map(int, input().split())
    if T == 1:
        if flip:
            A = A - N if A > N else A + N
            B = B - N if B > N else B + N
        S[A-1], S[B-1] = S[B-1], S[A-1]
    else:
        flip = not flip
if flip:
    S = S[N:] + S[:N]
print(*S, sep="")
    

