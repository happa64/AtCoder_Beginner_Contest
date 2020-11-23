# https://atcoder.jp/contests/iroha2019-day1/submissions/18368909
# F - Head of The Dragon
import sys

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
    res.sort()
    return res


def resolve():
    n, k = map(int, input().split())

    P = prime_factorization(n)
    t = sum([ex for _, ex in P])
    if t < k:
        print(-1)
        exit()

    res = []
    for p, ex in P:
        for _ in range(ex):
            if len(res) != k:
                res.append(p)
            else:
                res[-1] *= p

    print(*res)


if __name__ == '__main__':
    resolve()
