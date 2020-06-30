# https://atcoder.jp/contests/code-festival-2014-quala/submissions/13586834
# C - 2月29日
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b = map(int, input().split())

    b_4 = b // 4
    b_100 = b // 100
    b_400 = b // 400
    uruu_b = b_4 - (b_100 - b_400)

    a_4 = (a - 1) // 4
    a_100 = (a - 1) // 100
    a_400 = (a - 1) // 400
    uruu_a = a_4 - (a_100 - a_400)

    res = uruu_b - uruu_a
    print(res)


if __name__ == '__main__':
    resolve()
