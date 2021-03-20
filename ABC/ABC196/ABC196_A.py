# https://atcoder.jp/contests/abc196/submissions/21060002
# A - Difference Max
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    a, b = map(int, input().split())
    c, d = map(int, input().split())

    res = b - c
    print(res)


if __name__ == '__main__':
    solve()
