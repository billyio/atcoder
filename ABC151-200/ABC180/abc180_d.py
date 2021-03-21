X, Y, A, B = map(int, input().split())

n = 0
while X * A <= X + B and X * A < Y:
    X *= A
    n += 1

print((Y-X-1) // B + n)