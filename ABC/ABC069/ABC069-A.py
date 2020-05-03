# https://atcoder.jp/contests/abc069/tasks/abc069_a
# A - K-City
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    print((n - 1) * (m - 1))


if __name__ == '__main__':
    resolve()
