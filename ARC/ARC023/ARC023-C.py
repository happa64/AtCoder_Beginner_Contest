# https://atcoder.jp/contests/arc023/submissions/19741878
# C - タコヤ木
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


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    cmb = CmbMod(10 ** 9 + n, mod)
    res = 1
    left = 1
    i = 0
    while i < n:
        if A[i] == -1:
            cnt = 0
            while i < n and A[i] == -1:
                cnt += 1
                i += 1
            right = A[i]
            m = right - left + 1
            res *= cmb.cmb_mod(m + cnt - 1, cnt)
            res %= mod
        else:
            left = A[i]
            i += 1
    print(res)


if __name__ == '__main__':
    resolve()
