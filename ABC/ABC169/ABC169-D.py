# https://atcoder.jp/contests/abc169/submissions/13817443
# D - Div Game
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
    L = prime_factorization(n)
    res = 0
    for v, ex in L:
        i = 1
        while ex >= 0:
            if ex - i < 0:
                break
            ex -= i
            res += 1
            i += 1

    print(res)


if __name__ == '__main__':
    resolve()
