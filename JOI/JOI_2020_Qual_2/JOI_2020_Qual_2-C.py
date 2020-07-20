# https://atcoder.jp/contests/joi2020yo1b/submissions/15326160
# C - 最頻値 (Mode)
import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    D = Counter(A)

    res = max([v for v in D.values()])
    print(res)


if __name__ == '__main__':
    resolve()
