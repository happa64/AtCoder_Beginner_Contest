# https://atcoder.jp/contests/tenka1-2012-qualA/submissions/13908989
# A - 算盤の書
import sys
from functools import lru_cache

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


@lru_cache(None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def resolve():
    n = int(input())
    print(fib(n + 1))


if __name__ == '__main__':
    resolve()
