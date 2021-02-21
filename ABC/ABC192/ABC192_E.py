# https://atcoder.jp/contests/abc192/submissions/20362641
# E - Train
import sys
from heapq import heappop, heappush

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')


def resolve():
    n, m, x, y = map(int, input().split())
    edge = [[] for _ in range(n)]
    for _ in range(m):
        a, b, t, k = map(int, input().split())
        edge[a - 1].append([t, k, b - 1])
        edge[b - 1].append([t, k, a - 1])

    dist = [f_inf] * n
    dist[x - 1] = 0
    used = [False] * n
    used[x - 1] = True
    edge_list = []
    for cost, mod, node in edge[x - 1]:
        heappush(edge_list, [cost, node])
    while len(edge_list):
        cost, node = heappop(edge_list)
        if not used[node]:
            used[node] = True
            dist[node] = cost
            for next_cost, next_mod, next_node in edge[node]:
                if not used[next_node]:
                    next_cost += ((cost + next_mod - 1) // next_mod) * next_mod
                    heappush(edge_list, [next_cost, next_node])

    res = dist[y - 1]
    print(res if res != f_inf else -1)


if __name__ == '__main__':
    resolve()
