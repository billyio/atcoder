S = input()

if len(S) == 1 and S.islower():
    print("Yes")
elif S[::2].islower() and S[1::2].isupper():
    print("Yes")
else:
    print("No")