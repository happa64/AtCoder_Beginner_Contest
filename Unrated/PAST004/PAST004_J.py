# https://atcoder.jp/contests/past202010-open/submissions/18011191
# J - ワープ
import sys
from heapq import *

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def dijkstra_heap(v, start, edge):
    """
    ダイクストラ法：計算量O(ElogV)
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
    n, m = map(int, input().split())
    X = list(map(int, input().split()))
    S = input().rstrip()
    edge = [[] for _ in range(n + 6)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        edge[a - 1].append([c, b - 1])
        edge[b - 1].append([c, a - 1])

    # n=Ain, n+1=Bin, n+2=Cin, n+3=Aout, n+4=Bout, n+5=Cout
    for i in range(n):
        if S[i] == "A":
            edge[i].append([0, n])
            edge[n + 3].append([0, i])
        elif S[i] == "B":
            edge[i].append([0, n + 1])
            edge[n + 4].append([0, i])
        else:
            edge[i].append([0, n + 2])
            edge[n + 5].append([0, i])

    edge[n].append([X[0], n + 4])
    edge[n].append([X[1], n + 5])
    edge[n + 1].append([X[0], n + 3])
    edge[n + 1].append([X[2], n + 5])
    edge[n + 2].append([X[1], n + 3])
    edge[n + 2].append([X[2], n + 4])

    res = dijkstra_heap(n + 6, 0, edge)
    print(res[n - 1])


if __name__ == '__main__':
    resolve()
