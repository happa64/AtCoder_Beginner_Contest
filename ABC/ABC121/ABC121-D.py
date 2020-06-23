# https://atcoder.jp/contests/abc121/submissions/14640549
# D - XOR World
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b = map(int, input().split())

    def f(n):
        if n % 4 == 0:
            return n
        elif n % 4 == 1:
            return 1
        elif n % 4 == 2:
            return ((n // 4) + 1) * 4 - 1
        else:
            return 0

    print(f(b) ^ f(a - 1))


if __name__ == '__main__':
    resolve()
