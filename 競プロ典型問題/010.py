# 累積和
N = int(input())

C, P = [0] * N, [0] * N
sum1, sum2 = [0] * (N+1), [0] * (N+1)
for i in range(N):
    C[i], P[i] = map(int, input().split())
    
for i in range(N):
    sum1[i+1] += sum1[i]
    sum2[i+1] += sum2[i]

    if C[i] == 1:
        sum1[i+1] += P[i]
    else:
        sum2[i+1] += P[i]

# print(sum1)
# print(sum2)
Q = int(input())
for i in range(Q):
    l, r = map(int, input().split())
    print(sum1[r] - sum1[l-1], sum2[r] - sum2[l-1])