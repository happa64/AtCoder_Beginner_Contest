# https://atcoder.jp/contests/abc210/submissions/24276327
# A - Cabbages
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n, a, x, y = map(int, input().split())
    res = 0
    for i in range(1, n + 1):
        if i > a:
            res += y
        else:
            res += x
    print(res)


if __name__ == '__main__':
    solve()
