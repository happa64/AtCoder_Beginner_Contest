# https://atcoder.jp/contests/abc022/submissions/14016352
# C - Blue Bird
import sys
from itertools import combinations

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    C = [[f_inf] * n for _ in range(n)]
    edge = []
    for _ in range(m):
        u, v, l = map(int, input().split())
        C[u - 1][v - 1] = l
        C[v - 1][u - 1] = l
        if u - 1 == 0:
            edge.append(v - 1)
        elif v - 1 == 0:
            edge.append(u - 1)

    for i in range(n):
        C[i][i] = 0

    for k in range(1, n):
        for i in range(1, n):
            for j in range(1, n):
                C[i][j] = min(C[i][j], C[i][k] + C[k][j])

    res = f_inf
    for i, j in combinations(edge, 2):
        dist = C[i][j] + C[0][i] + C[0][j]
        res = min(res, dist)

    print(res if res != f_inf else -1)


if __name__ == '__main__':
    resolve()
