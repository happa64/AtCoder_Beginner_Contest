# https://atcoder.jp/contests/abc073/submissions/12928887
# D - joisino's travel
import sys
from itertools import permutations

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m, r = map(int, input().split())
    R = list(map(int, input().split()))

    # C[i][j]：iからjの距離
    C = [[f_inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        C[i][i] = 0

    for i in range(m):
        a, b, c = map(int, input().split())
        C[a - 1][b - 1] = c
        C[b - 1][a - 1] = c

    # C[i][j]：iからjの最短経路に上書き（ワーシャルフロイド法）
    for k in range(n):
        for i in range(n):
            for j in range(n):
                C[i][j] = min(C[i][j], C[i][k] + C[k][j])

    # 町を訪れる順番を全探索する
    res = f_inf
    for pattern in permutations(R):
        cost = 0
        for k in range(r - 1):
            i, j = pattern[k], pattern[k + 1]
            cost += C[i - 1][j - 1]
        res = min(res, cost)

    print(res)


def resolve2():
    import numpy as np
    from scipy.sparse import csr_matrix
    from scipy.sparse.csgraph import floyd_warshall
    from itertools import permutations

    n, m, r = map(int, input().split())
    R = list(map(lambda x: int(x) - 1, input().split()))
    edge = np.array([input().split() for _ in range(m)], dtype=np.int64).T
    graph = csr_matrix((edge[2], edge[:2] - 1), shape=(n, n))
    dist = floyd_warshall(graph, directed=False)

    res = f_inf
    for pattern in permutations(R):
        tot = 0
        for i in range(1, r):
            prev, now = pattern[i - 1], pattern[i]
            tot += dist[prev][now]
        res = min(res, tot)
    print(int(res))


if __name__ == '__main__':
    resolve()
