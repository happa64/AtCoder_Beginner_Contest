# https://atcoder.jp/contests/abc131/submissions/13123989
# C - Anti-Division
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def resolve():
    a, b, c, d = map(int, input().split())

    l = lcm(c, d)

    def calc(n):
        res = n // c + n // d - n // l
        return n - res

    print(calc(b) - calc(a - 1))


if __name__ == '__main__':
    resolve()
