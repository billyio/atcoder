import math

N= int(input())
x0, y0 = map(int, input().split())
xn2, yn2 = map(int, input().split())

x_center, y_center = (x0 + xn2) / 2, (y0 + yn2) / 2

x, y = x0 - x_center, y0 - y_center
cos=math.cos(2*math.pi/N)
sin=math.sin(2*math.pi/N)

x1 = cos * x - sin * y
y1 = sin * x + cos * y
x1 += x_center
y1 += y_center
print(x1,y1)