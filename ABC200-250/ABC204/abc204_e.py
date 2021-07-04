left, right = map(int, input().split())
left = max(2, left)
xk = [0] + [right // k - (left - 1) // k for k in range(1, right + 1)]
gk = [i ** 2 for i in xk]
for k in range(right, 1, -1):
    gk[k] -= sum(gk[k * 2:right + 1:k])
for i in range(left, right + 1):
    gk[i] -= 2 * xk[i] - 1


print(xk)
print(gk)
print(sum(gk[2:]))