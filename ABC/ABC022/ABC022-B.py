# https://atcoder.jp/contests/abc022/submissions/13586223
# B - Bumble Bee
import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(int(input()) for _ in range(n))
    D = Counter(A)

    res = 0
    for v in D.values():
        if v >= 2:
            res += v - 1

    print(res)


if __name__ == '__main__':
    resolve()
