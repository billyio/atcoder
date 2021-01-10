N, Q = map(int,input().split())
A = [0] + list(map(int,input().split()))

# print(N, Q)
# print(A)
# print("----")

for i in range(Q):
    t, x, y = map(int,input().split())
    if t == 1:
        A[x] = A[x] ^ y
    if t == 2:
        xor_list = A[x:-1] + [y]
        for j in range(len(xor_list)-1):
            res = xor_list[j] ^ xor_list[j+1]
        print(res)