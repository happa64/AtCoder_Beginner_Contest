# https://atcoder.jp/contests/abc041/submissions/13939113
# B - 直方体
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, c = map(int, input().split())
    res = a % mod * b % mod * c % mod
    print(res % mod)


if __name__ == '__main__':
    resolve()
