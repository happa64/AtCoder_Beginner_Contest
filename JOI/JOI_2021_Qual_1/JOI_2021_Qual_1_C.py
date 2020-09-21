# https://atcoder.jp/contests/joi2021yo1a/submissions/16942938
# C - 共通要素 (Common Elements)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    A = set(list(map(int, input().split())))
    B = set(list(map(int, input().split())))

    res = sorted([a for a in A if a in B])
    print(*res, sep="\n")


if __name__ == '__main__':
    resolve()
