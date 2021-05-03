# https://atcoder.jp/contests/typical90/submissions/22165273
# 022 - Cubic Cake（★2）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def solve():
    a, b, c = map(int, input().split())
    g = gcd(a, gcd(b, c))
    res = a // g + b // g + c // g - 3
    print(res)


if __name__ == '__main__':
    solve()
