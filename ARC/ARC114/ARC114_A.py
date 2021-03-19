# https://atcoder.jp/contests/arc114/submissions/21033096
# A - Not coprime
import sys
from itertools import product, accumulate

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


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


def prime_factorization(n):
    res = []
    for i in range(2, int(pow(n, 0.5) + 1)):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            res.append([i, cnt])
    if n and n != 1:
        res.append([n, 1])
    return res


def solve():
    _ = int(input())
    X = list(map(int, input().split()))

    primes = []
    for x in X:
        pf = prime_factorization(x)
        primes.append([p for p, ex in pf])

    er = Eratosthenes(50)
    all_primes = er.return_primes()
    res = f_inf
    for pattern in product([0, 1], repeat=len(all_primes)):
        use = set(all_primes[i] for i, p in enumerate(pattern) if p)
        for prime in primes:
            for p in prime:
                if p in use:
                    break
            else:
                break
        else:
            res = min(res, list(accumulate(use, func=lambda x, y: x * y))[-1])
    print(res)


if __name__ == '__main__':
    solve()
