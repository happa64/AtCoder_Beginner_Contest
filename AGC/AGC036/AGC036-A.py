# https://atcoder.jp/contests/agc036/tasks/agc036_a
# A - Triangle
import sys

sys.setrecursionlimit(10 ** 9)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = int(input())

    x3 = (-s) % (10 ** 9)
    y3 = (s + x3) // (10 ** 9)

    print(0, 0, 10 ** 9, 1, x3, y3)


if __name__ == '__main__':
    resolve()
