# import sys

# input = sys.stdin.readline
# N = int(input())
# XY = [list(map(int,input().split())) for _ in range(N)]
# M = int(input())
# op = [list(map(int,input().split())) for _ in range(M)]
# Q = int(input()) 
# AB = [list(map(int,input().split())) for _ in range(Q)]

# # x = x*cosθ - y*sinθ
# # y = x*sinθ + y*cosθ
# # θは反時計回り

# # 時計周りに90 θ=270
# def op1(xy):
#     return [-xy[1]*(-1), xy[0]*(-1)]

# # 反時計回りに90 θ=90
# def op2(xy):
#     return [-xy[1], xy[0]]

# # x=pについて対称移動
# def op3(xy, p):
#     if xy[0] == p:
#         return xy
#     elif xy[0] > p:
#         return [xy[0]-abs(xy[0]-p)*2, xy[1]]
#     else:
#         return [xy[0]+abs(xy[0]-p)*2, xy[1]]

# # y=pについて対称移動
# def op4(xy, p):
#     if xy[1] == p:
#         return xy
#     elif xy[1] > p:
#         return [xy[0], xy[1]-abs(xy[1]-p)*2]
#     else:
#         return [xy[0], xy[1]+abs(xy[1]-p)*2]

# # results = [[[0,0] for n in range(N)] for m in range(M+1)]
# # results[0] = XY

# query = {}
# for a,b in AB:
#     if b not in query.items():
#         query[b] = a
#     elif b in query.items() and query[b] > a:
#         query[b] = a

# for num, count in query.items():
#     ans = XY[num-1]
#     for i in range(count):
#         if op[i][0] == 1:
#             ans = op1(ans)
#             # results[i+1][num-1] = ans
#         elif op[i][0] == 2:
#             ans = op2(ans)
#             # results[i+1][num-1] = ans
#         elif op[i][0] == 3:
#             ans = op3(ans, op[i][1])
#             # results[i+1][num-1] = ans
#         elif op[i][0] == 4:
#             ans = op4(ans, op[i][1])
#             # results[i+1][num-1] = ans
#     print(ans)

# # for a,b in AB:
# #     x, y = results[a][b-1][0], results[a][b-1][1]
# #     print(x, y)

# # 全ての処理を行ってからクエリ部分を抜き出す→TLE
# # for i in range(M):
# #     for j in range(N):
# #         if op[i][0] == 1:
# #             results[i+1][j] = op1(results[i][j])
# #         elif op[i][0] == 2:
# #             results[i+1][j] = op2(results[i][j])
# #         elif op[i][0] == 3:
# #             results[i+1][j] = op3(results[i][j], op[i][1])
# #         elif op[i][0] == 4:
# #             results[i+1][j] = op4(results[i][j], op[i][1])


# # クエリ部分の処理のみ行う→TLE
# # for a,b in AB:
# #     if sum(results[a][b-1]) != 0:
# #         print(results[a][b-1][0], results[a][b-1][1])
# #     else:
# #         ans = XY[b-1]
# #         for i in range(a):
# #             if op[i][0] == 1:
# #                 ans = op1(ans)
# #                 results[a][i] = ans
# #             elif op[i][0] == 2:
# #                 ans = op2(ans)
# #                 results[a][i] = ans
# #             elif op[i][0] == 3:
# #                 ans = op3(ans, op[i][1])
# #                 results[a][i] = ans
# #             elif op[i][0] == 4:
# #                 ans = op4(ans, op[i][1])
# #                 results[a][i] = ans
# #         print(results)
# #         print(ans[0], ans[1])


# op〇〇回目までの処理それぞれの行列積を求めて、クエリごとに積
import numpy as np
from collections import defaultdict
import sys
 
input = sys.stdin.readline
 
n = int(input())
vv = [None] * n
for i in range(n):
    vv[i] = np.array(list(map(int, input().split())) + [1], dtype=np.int64).T

matrices = [
    np.array([
        [0, 1 ,0], 
        [-1, 0, 0], 
        [0, 0, 1]
    ], dtype=np.int64),
    np.array([
        [0, -1, 0],
        [1, 0, 0], 
        [0, 0, 1]
    ], dtype=np.int64),
    np.array([
        [-1, 0, 0], 
        [0, 1, 0], 
        [0, 0, 1]
    ], dtype=np.int64),
    np.array([
        [1, 0, 0], 
        [0, -1, 0], 
        [0, 0, 1]
    ], dtype=np.int64),
]
 
m = int(input())
 
r = [None] * (m + 1)
r[0] = np.identity(3, dtype=np.int64)
 
for i in range(m):
    op = list(map(int, input().split()))
 
    if op[0] == 1:
        r[i + 1] = matrices[0] @ r[i]
    elif op[0] == 2:
        r[i + 1] = matrices[1] @ r[i]
    elif op[0] == 3:
        matrices[2][0, 2] = op[1] * 2
        r[i + 1] = matrices[2] @ r[i]
    elif op[0] == 4:
        matrices[3][1, 2] = op[1] * 2
        r[i + 1] = matrices[3] @ r[i]

q = int(input())
for i in range(q):
    a, b = map(int, input().split())
    v = (r[a] @ vv[b - 1]).reshape([-1])
    print(f'{v[0]} {v[1]}')