s = input()
o, x, q = [], [], []
for i in range(10):
    if s[i] == "o":
        o.append(s[i])
    elif s[i] == "x":
        x.append(s[i])
    else:
        q.append(s[i])

if len(o) > 4:
    print(0)
else:
    ans = (1 ** len(o)) * (len(q) ** 2)
    
    print(ans) 