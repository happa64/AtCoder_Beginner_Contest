# https://atcoder.jp/contests/abc176/submissions/16095722
# A - Takoyaki
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, x, t = map(int, input().split())
    res = (n + x - 1) // x * t
    print(res)


if __name__ == '__main__':
    resolve()
