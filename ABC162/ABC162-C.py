# https://atcoder.jp/contests/abc162/tasks/abc162_c
# C - Sum of gcd of Tuples (Easy)
import sys
from math import gcd
sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    k = int(input())

    res = 0
    for a in range(1, k + 1):
        for b in range(1, k + 1):
            g1 = gcd(a, b)
            for c in range(1, k + 1):
                g2 = gcd(g1, c)
                res += g2

    print(res)


if __name__ == '__main__':
    resolve()
