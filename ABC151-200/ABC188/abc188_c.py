# ac
N = int(input())
A = list(map(int,input().split()))

mid = int(2**N/2)
left, right = A[:mid], A[mid:]
second = min(max(left), max(right))
print(A.index(second)+1)