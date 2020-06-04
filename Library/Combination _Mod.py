class Cmb:
    def __init__(self, n, r, p):
        """
        二項係数nCr(n個の区別できるものからr個のものを選ぶ組み合わせの数)をpで割った余りを求める
        :param n:全ての要素数
        :param r:選ぶ個数
        :param p:割る数。フェルマーの小定理を利用している為、素数である必要あり。
        """
        self.n = n
        self.r = r
        self.p = p
        self.fact = [1, 1]
        self.factinv = [1, 1]
        self.inv = [0, 1]

    def cmb_mod(self):
        """
        二項係数nCr(mod p)をO(r)にて計算。nが大きいがrは小さい時に使用。
        :return: nCr(mod p)
        """
        numer, denom = 1, 1
        for i in range(self.r):
            numer = (numer * (self.n - i)) % self.p
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

    def cmb_mod_with_prep(self):
        """
        二項係数nCr(mod p)をO(1)で求める。事前にprepを実行する事。
        :return: nCr(mod p)
        """
        if (self.r < 0) or (self.n < self.r):
            return 0
        self.r = min(self.r, self.n - self.r)
        return self.fact[self.n] * self.factinv[self.r] * self.factinv[self.n - self.r] % self.p
