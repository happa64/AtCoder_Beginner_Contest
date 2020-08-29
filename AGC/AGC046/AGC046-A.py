# https://atcoder.jp/contests/agc046/submissions/14496628
# A - Takahashikun, The Strider
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x = int(input())
    if 360 % x == 0:
        res = 360 // x
        print(res)
    else:
        q, r = divmod(360, x)
        print((360 // r) * q)


if __name__ == '__main__':
    resolve()
