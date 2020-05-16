# https://atcoder.jp/contests/abc113/submissions/13259532
# A - Discount Fare
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x, y = map(int, input().split())
    print(x + y // 2)


if __name__ == '__main__':
    resolve()
