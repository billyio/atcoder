N, M = map(int, input().split())
H = list(map(int, input().split()))
W = list(map(int, input().split()))
H.sort()

sum1 = [H[i + 1] - H[i] for i in range(N - 1)]
sum2 = sum1[1::2] + [0]
sum1 = [0] + sum1[::2]
print(sum1)
print(sum2)