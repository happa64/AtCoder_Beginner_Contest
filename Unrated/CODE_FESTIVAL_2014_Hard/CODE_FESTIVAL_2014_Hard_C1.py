# https://atcoder.jp/contests/code-festival-2014-morning-middle/submissions/18683095
# C - eject
import sys
from decimal import Decimal
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    p, n = map(str, input().split())
    p = Decimal(p)
    n = int(n)
    res = Decimal(0.5) + (p - Decimal(0.5)) * Decimal(pow(Decimal(1 - 2 * p), n - 1))
    print(res)


if __name__ == '__main__':
    resolve()
