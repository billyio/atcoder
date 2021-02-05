# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# A.append(0)
# A.append(N)
# A = list(set(A))
# A.sort()
# # print(A)

# k = 10 ** 9
# for i in range(len(A)-1):
#     print(A[i+1])
#     if A[i+1]-A[i] > 1:
#         k = min(k, A[i+1]-A[i]-1)
# # print(k)

# count = 0
# for j in range(len(A)-1):
#     if A[j+1]-A[j] == 1:
#         # print("skip")
#         continue
#     if (A[j+1]-A[j]-1) % k != 0:
#         count += int((A[j+1]-A[j]-1) // k) + 1
#     else:
#         count += int((A[j+1]-A[j]-1)) // k

# print(count)

import math

N,M = map(int,input().split())
A = list(map(int,input().split()))

if N == M:
    print(0)
    exit()
if M == 0:
    print(1)
    exit()


A.append(0)
A.append(N+1)
A.sort()

B = []
for i in range(len(A)-1):
    b = A[i+1]-A[i]-1
    B.append(b)
B = [b for b in B if b!=0]

cnt = 0
mi = min(B)
for i in range(len(B)):
    cnt += math.ceil(B[i]/mi)
print(cnt)