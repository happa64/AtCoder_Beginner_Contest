# https://atcoder.jp/contests/abc120/submissions/13620340
# C - Unification
import sys
import numpy as np
from collections import Counter, deque

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    red = s.count("0")
    blue = s.count("1")
    print(min(red, blue) * 2)


if __name__ == '__main__':
    resolve()
