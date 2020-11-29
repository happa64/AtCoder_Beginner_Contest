# https://atcoder.jp/contests/arc109/submissions/18460479
# A - Hands
import sys

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


def resolve():
    a, b, x, y = map(int, input().split())
    edge = [[] for _ in range(210)]
    for i in range(1, 101):
        edge[i].append([x, i + 100])
        edge[i + 100].append([x, i])

    for i in range(1, 100):
        edge[i + 1].append([x, i + 100])
        edge[i + 100].append([x, i + 1])

        edge[i].append([y, i + 1])
        edge[i + 1].append([y, i])

        edge[i + 100].append([y, i + 101])
        edge[i + 101].append([y, i + 100])

    res = dijkstra_heap(210, a, edge)
    print(res[b + 100])


if __name__ == '__main__':
    resolve()
