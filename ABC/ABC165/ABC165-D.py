# https://atcoder.jp/contests/abc165/tasks/abc165_d
# D - Floor Function
import sys
import math
sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, n = map(int, input().split())

    if b - 1 <= n:
        res = a - math.ceil(a / b)
        print(res)
    else:
        res = (a * n) // b - a * (n // b)
        print(res)


if __name__ == '__main__':
    resolve()
