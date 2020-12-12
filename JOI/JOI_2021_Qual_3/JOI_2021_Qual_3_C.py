# https://atcoder.jp/contests/joi2021yo1c/submissions/18697192
# C - 比較 (Comparison)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    res = sum([a <= b for a in A for b in B])
    print(res)


if __name__ == '__main__':
    resolve()
