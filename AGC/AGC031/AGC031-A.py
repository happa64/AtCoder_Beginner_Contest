# https://atcoder.jp/contests/agc031/submissions/11427739
# A - Colorful Subsequence
import sys
from collections import Counter
sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    s = input()
    D = Counter(s)
    res = 1
    for v in D.values():
        res = res * (v + 1) % mod
    print(res - 1)


if __name__ == '__main__':
    resolve()
