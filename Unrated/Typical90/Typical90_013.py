# https://atcoder.jp/contests/typical90/submissions/21909608
# 013 - Passing（★5）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def dijkstra_heap(n, start, edge):
    """
    疎なグラフの単一始点最短路を求める。O(|E|logN) *|E|は辺の数
    :param n: 走査するグラフの頂点数
    :param start: 始点
    :param edge: 重み付き隣接リスト。[cost, node]の形で渡す
    :return: 始点から各頂点への最短距離
    """
    from heapq import heappop, heappush

    f_inf = float("inf")
    res = [f_inf] * n
    res[start] = 0
    used = [False] * n
    used[start] = True
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


def solve():
    n, m = map(int, input().split())
    edge = [[] for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        edge[a - 1].append([c, b - 1])
        edge[b - 1].append([c, a - 1])

    d = dijkstra_heap(n, 0, edge)
    dr = dijkstra_heap(n, n - 1, edge)
    res = [d[i] + dr[i] for i in range(n)]
    print(*res, sep="\n")


if __name__ == '__main__':
    solve()
