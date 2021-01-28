# https://atcoder.jp/contests/arc025/submissions/19742501
# C - ウサギとカメ
import sys
from heapq import heappop, heappush
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def dijkstra_heap(n, start, edge):
    res = [f_inf] * n
    res[start] = 0
    used = [False] * n
    used[start] = True
    edge_list = []
    for u in edge[start]:
        heappush(edge_list, u)
    while len(edge_list):
        cost, node = heappop(edge_list)
        if not used[node]:
            res[node] = cost
            used[node] = True
            for next_cost, next_node in edge[node]:
                if not used[next_node]:
                    heappush(edge_list, (next_cost + cost, next_node))
    return res


def resolve():
    n, m, r, t = map(int, input().split())
    edge = [[] for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        edge[a - 1].append((c, b - 1))
        edge[b - 1].append((c, a - 1))

    res = 0
    for i in range(n):
        dist = dijkstra_heap(n, i, edge)
        time_rabbit = [d * t for d in dist]
        time_turtle = [d * r for d in dist]
        time_turtle_sort = sorted(time_turtle)
        for j in range(n):
            if time_rabbit[j] == 0:
                continue
            idx = bisect_left(time_turtle_sort, time_rabbit[j])
            res += idx - 1
            if time_turtle[j] < time_rabbit[j]:
                res -= 1
    print(res)


if __name__ == '__main__':
    resolve()
