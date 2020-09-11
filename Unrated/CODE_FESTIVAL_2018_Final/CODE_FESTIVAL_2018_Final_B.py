# https://atcoder.jp/contests/code-festival-2018-final-open/submissions/16628842
# B - Theme Color
import sys
from math import log10, ceil

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    R = list(map(int, input().split()))

    fact = [0]
    for i in range(1, n + 1):
        fact.append(fact[-1] + log10(i))

    res = -fact[n] + sum([fact[r] for r in R]) + n * log10(m)
    print(ceil(res))


if __name__ == '__main__':
    resolve()
