a, b = map(int, input().split())
ans = a*b/100
if ans.is_integer(): 
    print(int(ans))
else:
    print(ans)