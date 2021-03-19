# https://atcoder.jp/contests/abc172/submissions/21035192
# E - NEQ
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


class CmbMod:
    def __init__(self, n, p):
        self.n = n
        self.p = p
        self.fact = [1, 1]
        self.fact_inv = [1, 1]
        self.inv = [0, 1]

    def calc_cmb_mod(self, n, r):
        numer, denom = 1, 1
        for i in range(r):
            numer = (numer * (n - i)) % self.p
            denom = (denom * (i + 1)) % self.p
        return (numer * pow(denom, self.p - 2, self.p)) % self.p

    def prep(self):
        for i in range(2, self.n + 1):
            self.fact.append((self.fact[-1] * i) % self.p)
            self.inv.append((-self.inv[self.p % i] * (self.p // i)) % self.p)
            self.fact_inv.append((self.fact_inv[-1] * self.inv[-1]) % self.p)

    def fact_mod(self, n, r):
        return self.fact[n] * self.fact_inv[n - r] % self.p

    def cmb_mod(self, n, r):
        if r < 0 or n < r:
            return 0
        r = min(r, n - r)
        return self.fact[n] * self.fact_inv[r] % self.p * self.fact_inv[n - r] % self.p


def resolve():
    n, m = map(int, input().split())

    cmb = CmbMod(m, MOD)
    cmb.prep()

    res = 0
    for k in range(n + 1):
        now = cmb.cmb_mod(n, k) * cmb.fact_mod(m, n) % MOD * cmb.fact_mod(m - k, n - k) % MOD
        if k % 2:
            now = -now
        res = (res + now) % MOD
    print(res)


if __name__ == '__main__':
    resolve()
