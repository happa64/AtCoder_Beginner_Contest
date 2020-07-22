# https://atcoder.jp/contests/code-formula-2014-final/submissions/15358101
# A - Code Formula 2015
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b = map(int, input().split())
    print(a * b)


if __name__ == '__main__':
    resolve()
