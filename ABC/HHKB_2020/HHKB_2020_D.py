# https://atcoder.jp/contests/hhkb2020/submissions/17320507
# D - Squares
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())

        cnt_a = pow(n - a + 1, 2, mod)
        cnt_b = pow(n - b + 1, 2, mod)

        if n - a - b < 0:
            x4 = 0
        else:
            x4 = (n - a - b + 2) * (n - a - b + 1) % mod * pow(2, mod - 2, mod) % mod

        x3 = 2 * x4 % mod
        x2 = ((n - a + 1) * (n - b + 1) % mod - x3) % mod
        x1 = pow(x2, 2, mod)

        res = (cnt_a * cnt_b % mod - x1) % mod
        print(res % mod)


if __name__ == '__main__':
    resolve()
