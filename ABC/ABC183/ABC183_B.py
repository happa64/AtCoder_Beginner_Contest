# https://atcoder.jp/contests/abc183/submissions/18128316
# B - Billiards
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    sx, sy, gx, gy = map(int, input().split())
    dx = (gx - sx) / (sy + gy)
    print(sx + sy * dx)


if __name__ == '__main__':
    resolve()
