# https://atcoder.jp/contests/agc003/submissions/15716116
# C - BBuBBBlesort!
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = [int(input()) for _ in range(n)]
    A_S = sorted(A)
    IDX = defaultdict(int)
    for idx, a in enumerate(A_S):
        IDX[a] = idx + 1

    res = 0
    for i in range(n):
        if IDX[A[i]] % 2 != (i + 1) % 2:
            res += 1
    print(res // 2)


if __name__ == '__main__':
    resolve()
