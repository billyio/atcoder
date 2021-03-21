# import itertools

# S = [i for i in list(input())]
# for p in itertools.permutations(S):
#     num = int("".join(list(p)))
#     # print(num)
#     if num % 8 == 0:
#         print("Yes")
#         break
#     else:
#         continue
# else:
#     print("No")

# S = [i for i in list(input())]

# eight = [str(i*8).zfill(3) for i in range(125)]

# for p in itertools.permutations(S):
#     if str("".join(list(p)))[-3:].zfill(3) in eight:
#         print("Yes")
#         break
#     else:
#         continue
# else:
#     print("No")

from collections import Counter
n = input()
if len(n) <= 2:
    if int(n) % 8 == 0 or int(n[::-1]) % 8 == 0:
        print("Yes")
    else:
        print("No")
    exit()
cnt = Counter(n)
for i in range(112, 1000, 8):
    if not Counter(str(i)) - cnt:
        print("Yes")
        exit()
print("No")