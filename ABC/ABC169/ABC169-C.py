# https://atcoder.jp/contests/abc169/submissions/13921772?lang=ja
# C - Multiplication 3
import sys
import math
from decimal import Decimal
sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b = input().split()
    res = math.floor(Decimal(a) * Decimal(b))
    print(res)


if __name__ == '__main__':
    resolve()
