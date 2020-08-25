# https://atcoder.jp/contests/joisc2007/submissions/16226154
# score - 得点 (Score)
import sys
from bisect import bisect_right

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    S = list(int(input()) for _ in range(n))
    SS = sorted(S)

    for s in S:
        res = n - bisect_right(SS, s)
        print(res + 1)


if __name__ == '__main__':
    resolve()
