# https://atcoder.jp/contests/arc026/submissions/16480204
# C - 蛍光灯
import sys
from heapq import heapify, heappop, heappush

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
    n, L = map(int, input().split())
    edge = [[] for _ in range(L + 1)]
    for _ in range(n):
        l, r, c = map(int, input().split())
        edge[l].append([c, r])
        edge[r].append([c, l])
    for i in reversed(range(1, L + 1)):
        edge[i].append([0, i - 1])

    cost = dijkstra_heap(L + 1, 0, edge)
    print(cost[-1])


if __name__ == '__main__':
    resolve()
