N, K = map(int, input().split())
ans = N
for i in range(K):
    num_list = [int(n) for n in str(ans)]
    g1 = sorted(num_list, reverse=True)
    g1 = ''.join((str(g) for g in g1))
    g2 = sorted(num_list, reverse=False)
    g2 = ''.join((str(g) for g in g2))
    ans = int(g1) - int(g2)

print(ans)