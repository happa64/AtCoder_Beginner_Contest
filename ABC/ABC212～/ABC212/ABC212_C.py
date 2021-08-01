# https://atcoder.jp/contests/abc212/submissions/24654647
# C - Min Difference
import sys
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B.sort()

    res = f_inf
    for a in A:
        idx = bisect_left(B, a)
        if idx == 0:
            b = B[idx]
            diff = abs(a - b)
            res = min(res, diff)
        elif idx == m:
            idx -= 1
            b = B[idx]
            diff = abs(a - b)
            res = min(res, diff)
        else:
            b1 = B[idx - 1]
            b2 = B[idx]
            diff1 = abs(a - b1)
            diff2 = abs(a - b2)
            res = min(res, diff1, diff2)
    print(res)


if __name__ == '__main__':
    solve()
