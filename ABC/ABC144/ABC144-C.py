# https://atcoder.jp/contests/abc144/submissions/13455375
# C - Walk on Multiplication Table
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


# nの約数を列挙列挙する
def make_divisors(n):
    divisors = []
    for i in range(1, int(pow(n, 0.5)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors


def resolve():
    n = int(input())

    div = make_divisors(n)

    res = f_inf
    for i in div:
        cost = i + n // i - 2
        res = min(res, cost)

    print(res)


if __name__ == '__main__':
    resolve()
