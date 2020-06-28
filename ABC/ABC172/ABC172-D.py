# https://atcoder.jp/contests/abc172/submissions/14794465
# D - Sum of Divisors
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    L = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            L[j] += 1

    res = 0
    for i in range(1, n + 1):
        res += i * L[i]
    print(res)


def resolve2():
    def g(n):
        return ((n + 1) * n) // 2

    n = int(input())
    res = 0
    for i in range(1, n + 1):
        res += i * g(n // i)
    print(res)


if __name__ == '__main__':
    resolve2()
