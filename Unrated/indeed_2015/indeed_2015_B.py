# https://atcoder.jp/contests/indeednow-finala-open/submissions/20068384
# B - Office Ninja
import sys
from heapq import heappop, heappush

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
    r, c = map(int, input().split())
    grid = [list(map(lambda x: int(x) if x.isdigit() else x, input().rstrip())) for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if grid[i][j] == "s":
                s = i * c + j
                grid[i][j] = 0
            if grid[i][j] == "t":
                t = i * c + j
                grid[i][j] = 0

    edge = [[] for _ in range(r * c)]
    for i in range(r):
        for j in range(c):
            fr = i * c + j
            cost = grid[i][j]
            if i + 1 < r:
                edge[fr].append([grid[i + 1][j], (i + 1) * c + j])
                edge[(i + 1) * c + j].append([cost, fr])
            if j + 1 < c:
                edge[i * c + j].append([grid[i][j + 1], i * c + j + 1])
                edge[i * c + j + 1].append([cost, fr])
            if i % 2 and i + 1 < r and j + 1 < c:
                edge[i * c + j].append([grid[i + 1][j + 1], (i + 1) * c + (j + 1)])
                edge[(i + 1) * c + j + 1].append([cost, fr])
            if i % 2 == 0 and i + 1 < r and j - 1 >= 0:
                edge[i * c + j].append([grid[i + 1][j - 1], (i + 1) * c + (j - 1)])
                edge[(i + 1) * c + (j - 1)].append([cost, fr])

    dist = dijkstra_heap(r * c, s, edge)
    print(dist[t])


if __name__ == '__main__':
    resolve()
