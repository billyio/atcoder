# my answer
a, b = input().split()
sumA = sum(list(map(int, a)))
sumB = sum(list(map(int, b)))

if sumA >= sumB:
    print(sumA)
else:
    print(sumB)

A, B = input().split()
A = int(A[0]) + int(A[1]) + int(A[2])
B = int(B[0]) + int(B[1]) + int(B[2])
print(max(A, B))