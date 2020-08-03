# https://atcoder.jp/contests/arc034/submissions/15662323
# C - 約数かつ倍数
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def prime_factorization(n):
    """
    nを素因数分解します
    """
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


def resolve():
    a, b = map(int, input().split())

    prime = defaultdict(int)
    for i in range(b + 1, a + 1):
        primes = prime_factorization(i)
        for num, ex in primes:
            prime[num] += ex

    res = 1
    for v in prime.values():
        res *= (v + 1)
        res %= mod
    print(res)


if __name__ == '__main__':
    resolve()
