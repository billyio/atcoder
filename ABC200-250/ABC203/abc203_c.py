N, K = map(int, input().split())
balance = K
a_ = 0
AB = []
for i in range(N):
    a, b = map(int, input().split())
    AB.append([a, b])
AB.sort()

for i in range(N):
    a, b = AB[i][0], AB[i][1]
    # print(a_, "to", a)
    # have multiple friend in same place
    if a != a_:
        balance -= a - a_

    if balance < 0:
        print(a - abs(balance))
        break
    balance += b
    if balance < 0:
        print(a - abs(balance))
        break

    a_ = a

else:
    print(a + balance)