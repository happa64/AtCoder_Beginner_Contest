# https://atcoder.jp/contests/abc003/tasks/abc003_4
# D - AtCoder社の冬
import sys
from itertools import product
sys.setrecursionlimit(10 ** 7)


class ModComb:
    def __init__(self, MAX, mod=10 ** 9 + 7):
        fac = [1, 1]
        finv = [1, 1]
        inv = [0, 1]
        for i in range(2, MAX):
            fac.append(fac[i - 1] * i % mod)
            inv.append(mod - inv[mod % i] * (mod // i) % mod)
            finv.append(finv[i - 1] * inv[i] % mod)
        self.fac, self.finv, self.mod = fac, finv, mod

    def nCk(self, n, k):
        if n < k or n < 0 or k < 0:
            return 0
        fac, finv, mod = self.fac, self.finv, self.mod
        return fac[n] * (finv[k] * finv[n - k] % mod) % mod


def resolve():
    r, c = map(int, input().split())
    X, Y = map(int, input().split())
    D, L = map(int, input().split())
    mod = 10 ** 9 + 7
    k = (r - X + 1) * (c - Y + 1)

    m = ModComb(10 ** 5)
    if X * Y == D + L:
        c = m.nCk(X * Y, D)
    else:
        c = 0
        for pattern in product((0, 1), repeat=4):
            u, b, l, r = pattern
            x = X - l - r
            y = Y - u - b
            if x < 0 or y < 0:
                continue

            op = 1 if sum(pattern) % 2 == 0 else -1
            c += op * m.nCk(x * y, D + L) * m.nCk(D + L, D) % mod

    res = k * c % mod
    print(res)


if __name__ == '__main__':
    resolve()
