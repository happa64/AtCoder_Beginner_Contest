# https://atcoder.jp/contests/acl1/submissions/17216709
# B - Sum is Multiple
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def CRT(b1, m1, b2, m2):
    def extGcd(a, b):
        if a == 0:
            return b, 0, 1
        g, y, x = extGcd(b % a, a)
        return g, x - (b // a) * y, y

    d, p, q = extGcd(m1, m2)
    if (b2 - b1) % d != 0:
        return 0, -1
    m = m1 * (m2 // d)
    tmp = (b2 - b1) // d * p % (m2 // d)
    r = (b1 + m1 * tmp) % m
    return r, m


def make_divisors(n):
    divisors = []
    for i in range(1, int(pow(n, 0.5)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors


def resolve():
    n = int(input())
    div = make_divisors(2 * n)
    res = f_inf
    for x in div:
        y = 2 * n // x
        k = CRT(0, x, -1, y)
        if k[0] != 0:
            res = min(res, k[0])
    print(res)


if __name__ == '__main__':
    resolve()
