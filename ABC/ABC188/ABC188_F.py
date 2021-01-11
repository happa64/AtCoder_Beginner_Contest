# https://atcoder.jp/contests/abc188/submissions/19382265
# F - +1-1x2
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def f(y):
        if y == 1:
            return abs(y - x)

        if memo.get(y) is not None:
            return memo[y]

        if y % 2 == 0:
            memo[y] = min(f(y // 2) + 1, abs(y - x))
            return memo[y]
        else:
            memo[y] = min(f(y + 1) + 1, f(y - 1) + 1, abs(y - x))
            return memo[y]

    x, y = map(int, input().split())
    memo = defaultdict(int)
    print(f(y))


if __name__ == '__main__':
    resolve()
