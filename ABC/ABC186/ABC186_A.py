# https://atcoder.jp/contests/abc186/submissions/18859151
# A - Brick
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, w = map(int, input().split())
    res = n // w
    print(res)


if __name__ == '__main__':
    resolve()
