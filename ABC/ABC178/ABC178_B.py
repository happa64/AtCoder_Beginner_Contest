# https://atcoder.jp/contests/abc178/submissions/16676517
# B - Product Max
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, c, d = map(int, input().split())
    res = max(a * c, b * c, a * d, b * d)
    print(res)


if __name__ == '__main__':
    resolve()
