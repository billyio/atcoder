N = int(input())

if N < 10**1:
    print(0)
elif 10**1 <= N < 10**2:
    s, t = str(N)
    if t >= s:
        print(int(s))
    else:
        print(int(s)-1)
elif 10**2 <= N < 10**3:
    print(9)
elif 10**3 <= N < 10**4:
    s, t = str(N)[:2], str(N)[2:]
    if t >= s:
        print(int(s))
    else:
        print(int(s)-1)
elif 10**4 <= N < 10**5:
    print(99)
elif 10**5 <= N < 10**6:
    s, t = str(N)[:3], str(N)[3:]
    if t >= s:
        print(int(s))
    else:
        print(int(s)-1)
elif 10**6 <= N < 10**7:
    print(999)
elif 10**7 <= N < 10**8:
    s, t = str(N)[:4], str(N)[4:]
    if t >= s:
        print(int(s))
    else:
        print(int(s)-1)
elif 10**8 <= N < 10**9:
    print(9999)
elif 10**9 <= N < 10**10:
    s, t = str(N)[:5], str(N)[5:]
    if t >= s:
        print(int(s))
    else:
        print(int(s)-1)
elif 10**10 <= N < 10**11:
    print(99999)
elif 10**11 <= N < 10**12:
    s, t = str(N)[:6], str(N)[6:]
    if t >= s:
        print(int(s))
    else:
        print(int(s)-1)