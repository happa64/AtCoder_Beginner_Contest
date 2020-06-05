# https://atcoder.jp/contests/abc034/submissions/14014988
# B - ペア
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    if n % 2 == 0:
        print(n - 1)
    else:
        print(n + 1)


if __name__ == '__main__':
    resolve()
