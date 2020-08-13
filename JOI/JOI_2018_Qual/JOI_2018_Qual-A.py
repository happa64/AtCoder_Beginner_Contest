# https://atcoder.jp/contests/joi2018yo/submissions/15862608
# A - 鉛筆 (Pencils)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, a, b, c, d = map(int, input().split())
    res1 = ((n + a - 1) // a) * b
    res2 = ((n + c - 1) // c) * d
    print(min(res1, res2))


if __name__ == '__main__':
    resolve()
