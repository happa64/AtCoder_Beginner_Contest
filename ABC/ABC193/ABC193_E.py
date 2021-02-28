# https://atcoder.jp/contests/abc193/submissions/20555469
# E - Oversleeping
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def CRT(B, M):
    def extgcd(a, b):
        if b:
            d, y, x = extgcd(b, a % b)
            y -= (a // b) * x
            return d, x, y
        return a, 1, 0

    b1, m1 = 0, 1
    for b2, m2 in zip(B, M):
        d, p, q = extgcd(m1, m2)
        if (b2 - b1) % d != 0:
            return 0, -1
        tmp = (b2 - b1) // d * p % (m2 // d)
        b1 += m1 * tmp
        m1 *= m2 // d
    return b1 % m1, m1


def resolve():
    X, Y, P, Q = map(int, input().split())

    a = 2 * X + 2 * Y
    b = P + Q

    res = f_inf
    for t1 in range(X, X + Y):
        for t2 in range(P, P + Q):
            t, m = CRT([t1, t2], [a, b])
            if m == -1:
                continue
            res = min(res, t)
    print(res if res != f_inf else "infinity")


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        resolve()
