# https://atcoder.jp/contests/diverta2019/submissions/13655113
# A - Consecutive Integers
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    print(n - k + 1)


if __name__ == '__main__':
    resolve()
