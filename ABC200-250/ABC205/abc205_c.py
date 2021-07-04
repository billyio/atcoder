a, b, c = map(int, input().split())

if a >= 0 and b >= 0:
    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("=")
elif a >= 0 and b < 0:
    if c % 2 == 0:
        if abs(a) > abs(b):
            print(">")
        elif abs(a) < abs(b):
            print("<")
        else:
            print("=")
    else:
        print(">")
elif a < 0 and b>= 0:
    if c % 2 == 0:
        if abs(a) > abs(b):
            print(">")
        elif abs(a) < abs(b):
            print("<")
        else:
            print("=")
    else:
        print("<")
else:
    if abs(a) > abs(b):
        print("<")
    elif abs(a) < abs(b):
        print(">")
    else:
        print("=") 