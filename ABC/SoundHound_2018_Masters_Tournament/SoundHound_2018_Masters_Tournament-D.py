# https://atcoder.jp/contests/soundhound2018-summer-qual/submissions/16440821
# D - Saving Snuuk
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
    init = 10 ** 15
    n, m, s, t = map(int, input().split())
    edge_en = [[] for _ in range(n)]
    edge_sn = [[] for _ in range(n)]
    for _ in range(m):
        u, v, a, b = map(int, input().split())
        edge_en[u - 1].append([a, v - 1])
        edge_en[v - 1].append([a, u - 1])
        edge_sn[u - 1].append([b, v - 1])
        edge_sn[v - 1].append([b, u - 1])

    cost_en = dijkstra_heap(n, s - 1, edge_en)
    cost_sn = dijkstra_heap(n, t - 1, edge_sn)
    costs = []
    for i in range(n):
        total_cost = cost_en[i] + cost_sn[i]
        costs.append([total_cost, i])

    heapify(costs)
    cost = 0
    now = -1
    for i in range(n):
        while costs and now < i:
            if costs[0][1] < i:
                heappop(costs)
            else:
                cost, now = heappop(costs)
                break
        print(init - cost)


if __name__ == '__main__':
    resolve()
