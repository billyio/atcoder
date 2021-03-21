N = [int(i) for i in list(input())]
M = [i % 3 for i in N]

if sum(N) % 3 == 0:
    print(0)
elif sum(N) % 3 == 1 and len(N) == 1:
    print(-1)
elif sum(N) % 3 == 1 and M.count(1) >= 1:
    print(1)
elif sum(N) % 3 == 1 and M.count(2) >= 2 and len(N) >= 3:
    print(2)
elif sum(N) % 3 == 2 and len(N) == 1:
    print(-1)
elif sum(N) % 3 == 2 and M.count(2) >= 1:
    print(1)
elif sum(N) % 3 == 2 and M.count(1) >= 2 and len(N) >= 3:
    print(2)
else:
    print(-1)