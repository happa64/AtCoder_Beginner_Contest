# https://atcoder.jp/contests/abc057/submissions/13455643
# C - Digits in Multiplication
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    def f(a, b):
        return max(len(str(a)), len(str(b)))

    res = f_inf
    for a in range(1, int(pow(n, 0.5)) + 1):
        if n % a == 0:
            b = n // a
            t = f(a, b)
            res = min(res, t)

    print(res)


if __name__ == '__main__':
    resolve()
