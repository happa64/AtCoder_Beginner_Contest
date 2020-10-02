# https://atcoder.jp/contests/code-festival-2016-qualb/submissions/17137977
# C - Gr-idian MST
import sys
from bisect import bisect_left
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    W, H = map(int, input().split())
    P = list(int(input()) for _ in range(W))
    Q = list(int(input()) for _ in range(H))
    P.sort()
    Q.sort()
    R = [0] + list(accumulate(Q))

    res = sum(P + Q)
    for p in P:
        idx = bisect_left(Q, p)
        cost = (H - idx) * p
        diff = R[idx]
        res += cost + diff
    print(res)


if __name__ == '__main__':
    resolve()
