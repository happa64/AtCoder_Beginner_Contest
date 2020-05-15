# https://atcoder.jp/contests/abc072/submissions/13229286
# A - Sandglass2
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x, t = map(int, input().split())
    print(max(0,  x - t))


if __name__ == '__main__':
    resolve()
