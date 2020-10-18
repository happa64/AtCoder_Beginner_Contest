# https://atcoder.jp/contests/abc180/submissions/17441434
# C - Cream puff
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


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

    res = make_divisors(n)
    print(*res, sep="\n")


if __name__ == '__main__':
    resolve()
