# https://atcoder.jp/contests/abc021/submissions/15130636
# D - 多重ループ
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
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
            return self.fact[n] * self.factinv[r] * self.factinv[n - r] % self.p

    n = int(input())
    k = int(input())
    cmb = CmbMod(n - 1 + k, mod)
    cmb.prep()
    res = cmb.cmb_mod_with_prep(n - 1 + k, k)
    print(res % mod)


if __name__ == '__main__':
    resolve()
