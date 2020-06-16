# https://atcoder.jp/contests/arc048/submissions/14403224
# A - 階段の下
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b = map(int, input().split())

    if (a > 0 and b > 0) or (a < 0 and b < 0):
        print(b - a)
    else:
        print(b - a - 1)


if __name__ == '__main__':
    resolve()
