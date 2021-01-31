# AC
A,B,C = map(int, input().split())

if C == 0:
    if A > B:
        print("Takahashi")
    else:
        print("Aoki")
if C == 1:
    if A < B:
        print("Aoki")
    else:
        print("Takahashi")
