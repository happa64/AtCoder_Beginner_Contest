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