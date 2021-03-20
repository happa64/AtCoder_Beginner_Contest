# https://atcoder.jp/contests/abc196/submissions/21063949
#B - Round Down
import sys
from decimal import Decimal
import math

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    x = Decimal(input())
    res = Decimal(math.floor(x))
    print(res)

if __name__ == '__main__':
    solve()
