N = int(input())

c = 0
for i in range(1, N):
    c += (N-1) // i
print(int(c))

    