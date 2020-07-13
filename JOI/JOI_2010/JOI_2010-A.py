# https://atcoder.jp/contests/joi2010ho/submissions/15223043
# A - 旅人
import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 5


def resolve():
    n, m = map(int, input().split())
    S = list(int(input()) for _ in range(n - 1))
    A = list(int(input()) for _ in range(m))

    R = [0] + list(accumulate(S))
    res = 0
    prev = 0
    for a in A:
        now = prev + a
        res += abs(R[now] - R[prev])
        res %= mod
        prev = now
    print(res)


if __name__ == '__main__':
    resolve()
