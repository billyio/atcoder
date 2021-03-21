k=int(input())

q=["1","2","3","4","5","6","7","8","9"]
x=9
for i in q:
    if x>100000:
        break
    x+=1
    a=i[-1]
    for j in ([-1,0,1]):
        bb=int(a)+j
        if bb<10 and bb>=0:
            q.append(i+str(bb))


print(q[k-1])