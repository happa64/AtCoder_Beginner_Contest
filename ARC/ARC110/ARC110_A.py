# https://atcoder.jp/contests/arc110/submissions/18573700
# A - Redundant Redundancy
import sys
from math import gcd

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def lcm(a, b):
    return a * b // gcd(a, b)


def resolve():
    n = int(input())
    res = 1
    for i in range(2, n + 1):
        res = lcm(res, i)
    res += 1
    print(res)


if __name__ == '__main__':
    resolve()
