# https://atcoder.jp/contests/abc180/submissions/17494177
# F - Unbranched
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


class CmbMod:
    def __init__(self, n, p):
        """
        二項係数nCr(n個の区別できるものからr個のものを選ぶ組み合わせの数)をpで割った余りを求める
        """
        self.n = n
        self.p = p
        self.fact = [1, 1]
        self.factinv = [1, 1]
        self.inv = [0, 1]

    def cmb_mod(self, n, r):
        """
        二項係数nCr(mod p)をO(r)にて計算。nが大きいがrは小さい時に使用。
        """
        numer, denom = 1, 1
        for i in range(r):
            numer = (numer * (n - i)) % self.p
            denom = (denom * (i + 1)) % self.p
        return (numer * pow(denom, self.p - 2, self.p)) % self.p

    def prep(self):
        """
        二項係数nCr(mod p)をO(1)で求める為の前処理をO(N)にて実行。
        """
        for i in range(2, self.n + 1):
            self.fact.append((self.fact[-1] * i) % self.p)
            self.inv.append((-self.inv[self.p % i] * (self.p // i)) % self.p)
            self.factinv.append((self.factinv[-1] * self.inv[-1]) % self.p)

    def cmb_mod_with_prep(self, n, r):
        """
        二項係数nCr(mod p)をO(1)で求める。事前にprepを実行する事。
        """
        if (r < 0) or (n < r):
            return 0
        r = min(r, n - r)
        return self.fact[n] * self.factinv[r] % self.p * self.factinv[n - r] % self.p


def f(X):
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N + 1):
        for j in range(M + 1):
            for k in range(1, X + 1):
                ni = i + k
                nj = j + k - 1
                if ni > N or nj > M:
                    break
                dp[ni][nj] += cmb.cmb_mod_with_prep(N - i - 1, k - 1) * path[k] % mod * dp[i][j] % mod
                dp[ni][nj] %= mod

            for k in range(2, X + 1):
                ni = i + k
                nj = j + k
                if ni > N or nj > M:
                    break
                dp[ni][nj] += cmb.cmb_mod_with_prep(N - i - 1, k - 1) * cycle[k] % mod * dp[i][j] % mod
                dp[ni][nj] %= mod

    return dp[-1][-1]


N, M, L = map(int, input().split())

cmb = CmbMod(N, mod)
cmb.prep()

path = [1] * (N + 1)
for i in range(3, N + 1):
    path[i] = path[i - 1] * i % mod
cycle = [0] + path

res = (f(L) - f(L - 1)) % mod
print(res)
