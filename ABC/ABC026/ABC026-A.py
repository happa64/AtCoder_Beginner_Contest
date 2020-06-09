# https://atcoder.jp/contests/abc026/submissions/14127227
# A - 掛け算の最大値
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    A = int(input())
    print((A // 2) ** 2)


if __name__ == '__main__':
    resolve()
