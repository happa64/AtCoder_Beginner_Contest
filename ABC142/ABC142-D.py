# https://atcoder.jp/contests/abc142/tasks/abc142_d
# D - Disjoint Set of Common Divisors
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7

# nの因数を返す
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

    prime = [1]
    for p in res:
        for _ in range(p[1]):
            prime.append(p[0])

    return prime


def resolve():
    a, b = map(int, input().split())
    # Aの因数とBの因数で重複してい数の個数を求める
    A = prime_factorization(a)
    B = prime_factorization(b)
    res = set(A) & set(B)
    print(len(res))


if __name__ == '__main__':
    resolve()
