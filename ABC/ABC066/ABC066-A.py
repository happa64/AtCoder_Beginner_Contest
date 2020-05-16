# https://atcoder.jp/contests/abc066/submissions/13259441
# A - ringring
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, c = map(int, input().split())
    print(min(a + b, a + c, b + c))


if __name__ == '__main__':
    resolve()
