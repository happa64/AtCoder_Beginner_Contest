# https://atcoder.jp/contests/arc008/submissions/18524313
# C - THE☆たこ焼き祭り2012
import sys
from math import hypot

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def dijkstra(n, start, edge):
    """
    密なグラフの単一始点最短路を求める。O(N^2)
    :param n: 頂点数
    :param start: 始点
    :param edge: 重み付き隣接リスト。[cost, node]の形で渡す
    :return: 始点から各頂点への最短距離
    """
    f_inf = float("inf")
    res = [f_inf] * n
    res[start] = 0
    used = [False] * n
    for _ in range(n):
        min_dist = f_inf
        min_v = -1
        for v in range(n):
            if not used[v] and res[v] < min_dist:
                min_dist = res[v]
                min_v = v
        if min_v == -1:
            break
        for u, d in enumerate(edge[min_v]):
            res[u] = min(res[u], res[min_v] + d)
        used[min_v] = True
    return res


def resolve():
    n = int(input())
    A = [list(map(int, input().split())) for _ in range(n)]

    if n == 1:
        print(0)
        exit()

    cost = [[0] * n for _ in range(n)]
    for i in range(n):
        x1, y1, t1, r1 = A[i]
        for j in range(n):
            if i == j:
                continue
            x2, y2, t2, r2 = A[j]
            c = hypot(x1 - x2, y1 - y2) / min(t1, r2)
            cost[i][j] = c

    dist = dijkstra(n, 0, cost)
    dist = sorted(dist[1:], reverse=True)

    res = 0
    for i in range(n - 1):
        t = dist[i] + i
        res = max(res, t)
    print("{:.6f}".format(res))


if __name__ == '__main__':
    resolve()
