# https://atcoder.jp/contests/abc030/submissions/13452033#
# B - 時計盤
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    t = 60 * n + m
    print(min((5.5 * t) % 360, 360 - (5.5 * t) % 360))


if __name__ == '__main__':
    resolve()
