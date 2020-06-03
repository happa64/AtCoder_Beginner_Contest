# https://atcoder.jp/contests/abc015/submissions/13147633
# C - 高橋くんのバグ探し
import sys
from itertools import product

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(n)]

    for pattern in product(list(range(k)), repeat=n):
        res = 0
        for i, j in enumerate(pattern):
            res ^= T[i][j]

        if res == 0:
            print("Found")
            break
    else:
        print("Nothing")


if __name__ == '__main__':
    resolve()
