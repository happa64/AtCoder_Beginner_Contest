# https://atcoder.jp/contests/abc103/submissions/13979523
# C - Modulo Summation
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
    A = list(map(int, input().split()))

    L = 1
    for i in range(n):
        L = lcm(L, A[i])

    res = 0
    for i in range(n):
        res += (L - 1) % A[i]

    print(res)


if __name__ == '__main__':
    resolve()
