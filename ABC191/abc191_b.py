# AC
n,x = map(int,input().split())
a = list(map(int,input().split()))
a = [i for i in a if i != x]
print(*a)