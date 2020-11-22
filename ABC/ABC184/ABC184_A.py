# https://atcoder.jp/contests/abc184/submissions/18303158
# A - Determinant
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    res = a * d - b * c
    print(res)


if __name__ == '__main__':
    resolve()
