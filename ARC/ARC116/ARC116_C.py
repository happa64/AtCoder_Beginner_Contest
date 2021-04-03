# https://atcoder.jp/contests/arc116/submissions/21480084
# C - Multiple Sequences
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


class Eratosthenes:
    def __init__(self, n):
        self.n = n
        self.min_factor = [-1] * (n + 1)
        self.min_factor[0], self.min_factor[1] = 0, 1
        self.primes = []
        self.get_primes()

    def get_primes(self):
        is_prime = [True] * (self.n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, self.n + 1):
            if not is_prime[i]:
                continue
            self.primes.append(i)
            self.min_factor[i] = i
            for j in range(i * 2, self.n + 1, i):
                is_prime[j] = False
                if self.min_factor[j] == -1:
                    self.min_factor[j] = i

    def return_primes(self):
        return self.primes

    def prime_factorization(self, n):
        res = []
        while n != 1:
            prime = self.min_factor[n]
            exp = 0
            while self.min_factor[n] == prime:
                exp += 1
                n //= prime
            res.append((prime, exp))
        return res


def solve():
    n, m = map(int, input().split())

    er = Eratosthenes(m)
    cmb = CmbMod(n + 100, MOD)
    cmb.prep()

    res = 0
    for i in range(1, m + 1):
        pf = er.prime_factorization(i)
        t = 1
        for _, ex in pf:
            t *= cmb.calc_cmb_mod(n + ex - 1, ex)
            t %= MOD
        res += t
        res %= MOD
    print(res)


if __name__ == '__main__':
    solve()
