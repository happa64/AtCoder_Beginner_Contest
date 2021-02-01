# https://atcoder.jp/contests/arc004/submissions/19865569
# D - 表現の自由 ( Freedom of expression )
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def prime_factorization(n):
    res = []
    for i in range(2, int(pow(n, 0.5)) + 1):
        if n % i == 0:
            ex = 0
            while n % i == 0:
                ex += 1
                n //= i
            res.append([i, ex])
    if n != 1:
        res.append([n, 1])
    return res


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


def resolve():
    n, m = map(int, input().split())
    pf = prime_factorization(abs(n))
    MAX = m + int(pow(abs(n), 0.5)) + 1
    cmb = CmbMod(MAX, mod)
    cmb.prep()
    res = 1
    for _, p in pf:
        res *= cmb.cmb_mod_with_prep(p + m - 1, p)
        res %= mod
    cnt = 0
    if n > 0:
        for i in range(0, m + 1, 2):
            cnt += cmb.cmb_mod_with_prep(m, i)
            cnt %= mod
    else:
        for i in range(1, m + 1, 2):
            cnt += cmb.cmb_mod_with_prep(m, i)
            cnt %= mod
    print(res * cnt % mod)


if __name__ == '__main__':
    resolve()
