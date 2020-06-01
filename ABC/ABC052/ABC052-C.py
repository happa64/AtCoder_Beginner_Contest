# https://atcoder.jp/contests/arc067/submissions/13927364
# C - Factors of Factorial
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


def resolve():
    n = int(input())

    P = [0] * 1000
    for i in range(1, n + 1):
        t = prime_factorization(i)
        for num, ex in t:
            P[num] += ex

    res = 1
    for p in P:
        res *= p + 1
        res % mod

    print(res % mod)


if __name__ == '__main__':
    resolve()
