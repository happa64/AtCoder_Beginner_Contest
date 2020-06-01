# https://atcoder.jp/contests/panasonic2020/submissions/13922060
# C - Sqrt Inequality
import sys
from decimal import Decimal

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, c = input().split()
    print("Yes" if Decimal(a) ** Decimal("0.5") + Decimal(b) ** Decimal("0.5") < Decimal(c) ** Decimal("0.5") else "No")


if __name__ == '__main__':
    resolve()
