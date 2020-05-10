# https://atcoder.jp/contests/abc167/submissions/13044865
# C - Skill Up
import sys
from itertools import product

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m, x = map(int, input().split())
    C = [list(map(int, input().split())) for _ in range(n)]

    res = f_inf
    for pattern in product([0, 1], repeat=n):
        A = [0 for _ in range(m)]
        cost = 0
        for idx, p in enumerate(pattern):
            if p == 1:
                cost += C[idx][0]
                for i in range(m):
                    A[i] += C[idx][i + 1]

        for a in A:
            if a < x:
                break
        else:
            res = min(res, cost)

    if res == f_inf:
        print(-1)
    else:
        print(res)


if __name__ == '__main__':
    resolve()
