# https://atcoder.jp/contests/abc145/submissions/14029808
# D - Knight
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
        return self.fact[n] * self.factinv[r] * self.factinv[n - r] % self.p


def resolve():
    X, Y = map(int, input().split())

    cnt = (X + Y) // 3
    left = 0
    right = 0
    for i in range(cnt):
        if (i * 1 + (cnt - i) * 2 == X and i * 2 + (cnt - i) * 1 == Y) or (
                i * 1 + (cnt - i) * 2 == Y and i * 2 + (cnt - i) * 1 == X):
            left = i
            right = cnt - i
            break
    else:
        print(0)
        exit()

    cmb = CmbMod(cnt, mod)
    res = cmb.cmb_mod(cnt, min(left, right))
    print(res)


if __name__ == '__main__':
    resolve()
