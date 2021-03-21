# AC
N, M, T = map(int,input().split())
battery = N
tmp = 0

for _ in range(M):
    a, b = map(int,input().split())
    use = a-tmp
    if N-use <= 0:
        print("No")
        exit()
    else:
        N = N-use
        
    charge = b-a
    if N+charge > battery:
        N = battery
    else:
        N = N+charge
        
    tmp = b
    if N <= 0:
        print("No")
        exit()
    
if N-T+tmp > 0:
    print("Yes")
else:
    print("No")

# https://atcoder.jp/contests/abc185/submissions/18728108
n,m,t=map(int,input().split())
N=n
now=0
for i in range(m):
    a,b=map(int,input().split())
    n-=a-now
    if n<=0:exit(print("No"))
    n+=b-a
    n=min(n,N)
    now=b
n-=t-now
if n<=0:exit(print("No"))
print("Yes")