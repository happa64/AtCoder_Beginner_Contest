# https://atcoder.jp/contests/joisc2007/submissions/16238840
# factorial - 階乗 (Factorial)
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
    pf = prime_factorization(n)
    res = 0
    for p, ex in pf:
        tmp = 0
        while ex > 0:
            tmp += p
            t = tmp
            while t % p == 0:
                t //= p
                ex -= 1
        res = max(res, tmp)
    print(res)


if __name__ == '__main__':
    resolve()
