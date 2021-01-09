n = int(input())

dots = []
for _ in range(n):
    x, y = input().split()
    dots.append([int(x), int(y)])

dots.sort(key=lambda x:x[0])
count = 0

for i in range(n):
    # xi, xy = dots[i][0], dots[i][1]
    for j in range(n - i - 1):
        xi, yi = dots[i][0], dots[i][1]
        xj, yj = dots[i+j+1][0], dots[i+j+1][1]
        if xi == xj:
            continue
        if abs(xi - xj) >= abs(yi - yj):
            count += 1

print(count)