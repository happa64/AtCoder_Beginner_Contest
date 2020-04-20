# https://atcoder.jp/contests/abc142/tasks/abc142_a
# A - Odds of Oddness
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    if n % 2 == 0:
        print((n / 2) / n)
    else:
        print((n + 1) / 2 / n)


if __name__ == '__main__':
    resolve()
