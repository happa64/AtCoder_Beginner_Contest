# https://atcoder.jp/contests/abc035/submissions/15550673
# D - トレジャーハント
import sys
from heapq import heappop, heappush

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def dijkstra_heap(v, start, edge):
    """
    ダイクストラ法
    :param v: 走査するグラフの頂点数
    :param start: 始点
    :param edge: 重み付き隣接リスト。[cost, node]の形で渡す
    :return: 始点から各頂点への最短距離
    """
    res = [f_inf] * v
    res[start] = 0
    checked = [False] * v
    checked[start] = True
    edge_list = []
    for u in edge[start]:
        heappush(edge_list, u)
    while len(edge_list):
        min_edge = heappop(edge_list)
        cost, node = min_edge
        if not checked[node]:
            res[node] = cost
            checked[node] = True
            for next_cost, next_node in edge[node]:
                if not checked[next_node]:
                    heappush(edge_list, [next_cost + cost, next_node])
    return res


def resolve():
    n, m, t = map(int, input().split())
    A = list(map(int, input().split()))
    edge = [[] for _ in range(n)]
    edge_r = [[] for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        edge[a - 1].append([c, b - 1])
        edge_r[b - 1].append([c, a - 1])

    res = 0
    dist = dijkstra_heap(n, 0, edge)
    dist_r = dijkstra_heap(n, 0, edge_r)
    for i in range(n):
        d = dist[i] + dist_r[i]
        score = (t - d) * A[i]
        res = max(res, score)

    print(res)


if __name__ == '__main__':
    resolve()
