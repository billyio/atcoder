N = int(input())
A = list(map(int, input().split()))
A.sort()
Q = int(input())

def binary_search(num_list, a):
    max_n = len(num_list) - 1
    min_n = 0
    while max_n - min_n > 1:
        mid_n = (max_n + min_n) // 2
        if a < num_list[mid_n]:
            max_n = mid_n
        else:
            min_n = mid_n

    if abs(a - num_list[min_n]) > abs(a - num_list[max_n]):
        print(abs(a - num_list[max_n]))
    else:
        print(abs(a - num_list[min_n]))

for i in range(Q):
    B = int(input())
    binary_search(A, B)