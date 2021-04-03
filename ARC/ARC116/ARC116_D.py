# https://atcoder.jp/contests/arc116/submissions/21479026
# D - I Wanna Win The Game
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 998244353


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


def solve():
    n, m = map(int, input().split())

    l = m.bit_length() - 1
    cmb = CmbMod(n, MOD)
    cmb.prep()

    dp = [0] * (m + 1)
    for v in range(0, n + 1, 2):
        if v > m:
            break
        dp[v] = cmb.cmb_mod(n, v)

    k = 1
    for _ in range(1, l):
        k *= 2
        next_dp = [0] * (m + 1)
        for u in range(0, m + 1, 2):
            for v in range(0, n + 1, 2):
                if u + v * k > m:
                    break
                next_dp[u + v * k] += dp[u] * cmb.cmb_mod(n, v)
                next_dp[u + v * k] %= MOD
        dp = next_dp
    print(dp[m])


if __name__ == '__main__':
    solve()
