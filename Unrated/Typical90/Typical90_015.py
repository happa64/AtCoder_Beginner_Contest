# https://atcoder.jp/contests/typical90/submissions/22272096
# 015 - Don't be too close（★6）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


class CmbMod:
    def __init__(self, n, p, flg=True):
        self.n = n
        self.p = p
        self.fact = [1, 1]
        self.fact_inv = [1, 1]
        self.inv = [0, 1]
        if flg:
            self._prep()

    def _prep(self):
        for i in range(2, self.n + 1):
            self.fact.append((self.fact[-1] * i) % self.p)
            self.inv.append((-self.inv[self.p % i] * (self.p // i)) % self.p)
            self.fact_inv.append((self.fact_inv[-1] * self.inv[-1]) % self.p)

    def calc_cmb_mod(self, n, r):
        numer, denom = 1, 1
        for i in range(r):
            numer = (numer * (n - i)) % self.p
            denom = (denom * (i + 1)) % self.p
        return (numer * pow(denom, self.p - 2, self.p)) % self.p

    def fact_mod(self, n, r):
        return self.fact[n] * self.fact_inv[n - r] % self.p

    def cmb_mod(self, n, r):
        if r < 0 or n < r:
            return 0
        r = min(r, n - r)
        return self.fact[n] * self.fact_inv[r] % self.p * self.fact_inv[n - r] % self.p


def solve():
    n = int(input())
    cmb = CmbMod(n, MOD)
    for k in range(1, n + 1):
        res = 0
        limit = (n + k - 1) // k + 1
        for a in range(1, limit):
            res += cmb.cmb_mod(n - (a - 1) * (k - 1), a)
            res %= MOD
        print(res)


if __name__ == '__main__':
    solve()
