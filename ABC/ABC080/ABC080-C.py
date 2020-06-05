# https://atcoder.jp/contests/abc080/submissions/12861810
# C - Shopping Street
import sys
from itertools import product

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    F = [list(map(int, input().split())) for _ in range(n)]
    P = [list(map(int, input().split())) for _ in range(n)]

    res = -f_inf
    for pattern in product([0, 1], repeat=10):
        if sum(pattern) == 0:
            continue

        score = 0
        for f, p in zip(F, P):
            cnt = 0
            for i in range(10):
                if pattern[i] == f[i] == 1:
                    cnt += 1
            score += p[cnt]

        res = max(res, score)

    print(res)


if __name__ == '__main__':
    resolve()
