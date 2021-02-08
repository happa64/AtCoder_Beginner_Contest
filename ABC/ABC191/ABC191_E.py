# https://atcoder.jp/contests/abc191/submissions/19991718
# E - Come Back Quickly
import sys
from heapq import heappop, heappush

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def dijkstra_heap(n, start, edge):
    """
    疎なグラフの単一始点最短路を求める。O(|E|logN) *|E|は辺の数
    :param n: 走査するグラフの頂点数
    :param start: 始点
    :param edge: 重み付き隣接リスト。[cost, node]の形で渡す
    :return: 始点から各頂点への最短距離
    """
    res = [f_inf] * n
    used = [False] * n
    edge_list = []
    for u in edge[start]:
        heappush(edge_list, u)
    while len(edge_list):
        min_edge = heappop(edge_list)
        cost, node = min_edge
        if not used[node]:
            res[node] = cost
            used[node] = True
            for next_cost, next_node in edge[node]:
                if not used[next_node]:
                    heappush(edge_list, [next_cost + cost, next_node])
    return res


def resolve():
    n, m = map(int, input().split())
    edge = [[] for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        edge[a - 1].append([c, b - 1])

    for i in range(n):
        dist = dijkstra_heap(n, i, edge)
        res = dist[i]
        print(res if res != f_inf else -1)


if __name__ == '__main__':
    resolve()
