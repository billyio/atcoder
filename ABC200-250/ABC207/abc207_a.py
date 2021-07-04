a, b, c = map(int,input().split())
ans = sum([a,b,c]) - min([a,b,c])
print(ans)