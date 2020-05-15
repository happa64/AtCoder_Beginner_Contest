# https://atcoder.jp/contests/abc070/submissions/12942858
# D - Transit Tree Path
import sys
import heapq

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())

    edge = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b, c = map(int, input().split())
        edge[a - 1].append([c, b - 1])
        edge[b - 1].append([c, a - 1])

    q, k = map(int, input().split())
    Query = [list(map(int, input().split())) for _ in range(q)]

    def dijkstra_heap(s):
        # 始点sから各頂点への最短距離
        d = [float("inf")] * n
        used = [True] * n  # True:未確定
        d[s] = 0
        used[s] = False
        edgelist = []
        for e in edge[s]:
            heapq.heappush(edgelist, e)
        while len(edgelist):
            minedge = heapq.heappop(edgelist)
            # まだ使われてない頂点の中から最小の距離のものを探す
            if not used[minedge[1]]:
                continue
            v = minedge[1]
            d[v] = minedge[0]
            used[v] = False
            for e in edge[v]:
                if used[e[1]]:
                    heapq.heappush(edgelist, [e[0] + d[v], e[1]])
        return d

    dist = dijkstra_heap(k - 1)

    for x, y in Query:
        res = dist[x - 1] + dist[y - 1]
        print(res)


if __name__ == '__main__':
    resolve()
