# https://atcoder.jp/contests/abc169/tasks/abc169_a
# A - Multiplication 1
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b = map(int, input().split())
    print(a * b)


if __name__ == '__main__':
    resolve()
