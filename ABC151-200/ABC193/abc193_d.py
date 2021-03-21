K = int(input())
S = input()[:4]
T = input()[:4]
card = [K] * 10

for s in S:
    card[int(s)] -= 1
for t in T:
    card[int(t)] -= 1

all_comb = sum(card[1:]) * (sum(card[1:]) - 1)

def score(S):
    cnt = [0] * 10
    for c in S:
        cnt[int(c)] += 1
    ans = 0
    for i in range(1, 10):
        ans += i * 10 ** cnt[i]
    return ans

win_comb = 0
for i in range(1,10):
    if card[i] == 0:
        continue
    for j in range(1,10):
        if card[j] == 0:
            continue
        elif i == j and card[i] <= 1:
            continue

        if i == j and score(S + str(i)) > score(T + str(j)):
            win_comb += card[i] * (card[i] - 1)
        elif i != j and score(S + str(i)) > score(T + str(j)):
            win_comb += card[i] * card[j]

print(win_comb / all_comb)