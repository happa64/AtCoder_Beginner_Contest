# https://atcoder.jp/contests/abc051/submissions/12823217
# A - Haiku
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    res = s.replace(",", " ")
    print(res)


if __name__ == '__main__':
    resolve()
