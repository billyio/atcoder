N, W = map(int, input().split())

a = N % W
print(int((N-a) / W))