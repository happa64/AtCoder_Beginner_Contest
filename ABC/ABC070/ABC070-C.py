# https://atcoder.jp/contests/abc070/submissions/13979607
# C - Multiple Clocks
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def resolve():
    n = int(input())
    T = list(int(input()) for _ in range(n))

    res = 1
    for i in range(n):
        res = lcm(res, T[i])

    print(res)


if __name__ == '__main__':
    resolve()
