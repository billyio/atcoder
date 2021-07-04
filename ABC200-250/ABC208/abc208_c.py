n, k = map(int,input().split())
a = list(map(int,input().split()))
p, q = k % n, k // n

a_sort = sorted(a)
# print(p,q)


for i in range(n):
    if a[i] <= a_sort[p-1] and p > 0:
        print(q+1)
    else:
        print(q)