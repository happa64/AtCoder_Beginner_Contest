# https://atcoder.jp/contests/zone2021/submissions/22349189
# E - 潜入
import sys
from heapq import heappop, heappush

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
                    heappush(edge_list, (next_cost + cost, next_node))
    return res


def solve():
    H, W = map(int, input().split())
    A = tuple(tuple(map(int, input().split())) for _ in range(H))
    B = tuple(tuple(map(int, input().split())) for _ in range(H - 1))
    HW = H * W
    edge = [[] for _ in range(HW * 2)]
    for h in range(H):
        for w in range(W):
            v = h * W + w
            edge[v].append((1, HW + v))
            edge[HW + v].append((0, v))
            if w - 1 >= 0:
                edge[v].append((A[h][w - 1], h * W + w - 1))
            if w + 1 < W:
                edge[v].append((A[h][w], h * W + w + 1))
            if h - 1 >= 0:
                edge[HW + v].append((1, HW + (h - 1) * W + w))
            if h + 1 < H:
                edge[v].append((B[h][w], (h + 1) * W + w))
    res = dijkstra_heap(H * W * 2, 0, edge)
    print(res[HW - 1])


if __name__ == '__main__':
    solve()
