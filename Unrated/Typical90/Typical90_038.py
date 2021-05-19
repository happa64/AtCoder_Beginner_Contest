# https://atcoder.jp/contests/typical90/submissions/22536922
# 038 - Large LCM（★3）
import sys
from math import gcd

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    a, b = map(int, input().split())
    res = a * b // gcd(a, b)
    print("Large" if res > 10 ** 18 else res)


if __name__ == '__main__':
    solve()
