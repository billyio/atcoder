# WC
# A, B, W = map(int, input().split())
# W = W * 1000

# mi, mx = W // B, W // A

# a_, b_ = 0, mi
# total = a_ * A + b_ * B

# while b_> 0:
#     tmp = W - b_ * B
#     a_ = tmp // A
#     for i in range(a_):
#         total = a_ * A + b_ * B 
#         if total == W:
#             mi, mx = b_, i
#             print(mi, mx)
#     b_ += 1

import math
a,b,w=map(int,input().split())
upper=int(math.floor(1000*w/a))
lower=int(math.ceil(1000*w/b))
print(upper, lower)
if lower>upper:
  print("UNSATISFIABLE")
else:
  print(lower,upper)