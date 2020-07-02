# https://atcoder.jp/contests/abc156/submissions/13575929
# D - Bouquet
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, a, b = map(int, input().split())

    def cmb_mod(n, r, mod):
        x, y = 1, 1
        for i in range(r):
            x = (x * (n - i)) % mod
            y = (y * (i + 1)) % mod
        return (x * pow(y, mod - 2, mod)) % mod

    total = pow(2, n, mod) - 1
    res = total - cmb_mod(n, a, mod) - cmb_mod(n, b, mod)
    print(res % mod)


if __name__ == '__main__':
    resolve()
