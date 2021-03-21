S = input()
T = input()



S = bin(int("0b" + S, 2))
T = bin(int("0b" + T, 2))
print(S, T)
print(len(S))

mi = 10**10

for i in range(len(S)-len(T)+1):
    print(S[i:len(T)])