# https://atcoder.jp/contests/abc178/submissions/16695086
# C - Ubiquity
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    if n == 1:
        print(0)
        exit()

    res = pow(10, n, mod) - (pow(9, n, mod) + pow(9, n, mod) - pow(8, n, mod))
    print(res % mod)


if __name__ == '__main__':
    resolve()
