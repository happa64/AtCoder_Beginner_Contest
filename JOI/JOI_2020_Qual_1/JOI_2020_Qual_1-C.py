# https://atcoder.jp/contests/joi2020yo1a/submissions/15316525
# C - マージ (Merge)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = sorted(A + B)
    print(*C, sep="\n")


if __name__ == '__main__':
    resolve()
