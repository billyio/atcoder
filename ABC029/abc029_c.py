from itertools import product

def main():
    n = int(input())
    res = []
    for ss in product('abc', repeat=n):
        res.append(''.join(ss))
    
    print('\n'.join(res))