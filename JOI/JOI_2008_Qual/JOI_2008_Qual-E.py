# https://atcoder.jp/contests/joi2008yo/submissions/14935371
# E - おせんべい
import sys
from itertools import product
from copy import deepcopy

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    r, c = map(int, input().split())
    A_init = [list(map(int, input().split())) for _ in range(r)]

    res = 0
    for pattern in product([0, 1], repeat=r):
        A = deepcopy(A_init)
        for idx, p in enumerate(pattern):
            if p == 1:
                for i in range(c):
                    A[idx][i] ^= 1
        cnt = [0] * c
        for i in range(r):
            for j in range(c):
                cnt[j] += A[i][j]
        total = 0
        for i in cnt:
            total += max(i, r - i)
        res = max(res, total)
    print(res)


if __name__ == '__main__':
    resolve()
