# https://atcoder.jp/contests/abc079/submissions/15119609
# D - Wall
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    cost = [list(map(int, input().split())) for _ in range(10)]
    grid = [list(map(int, input().split())) for _ in range(H)]

    for k in range(10):
        for i in range(10):
            for j in range(10):
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

    res = 0
    for h in range(H):
        for w in range(W):
            if grid[h][w] == -1 or grid[h][w] == 1:
                continue
            num = grid[h][w]
            res += cost[num][1]
    print(res)


def resolve2():
    import numpy as np
    from scipy.sparse.csgraph import floyd_warshall

    h, w = map(int, input().split())
    graph = np.array([list(map(int, input().split())) for _ in range(10)])
    A = tuple(tuple(map(int, input().split())) for _ in range(h))

    dist = floyd_warshall(graph)
    res = sum(dist[A[i][j]][1] if A[i][j] != -1 else 0 for i in range(h) for j in range(w))
    print(int(res))


if __name__ == '__main__':
    resolve()
