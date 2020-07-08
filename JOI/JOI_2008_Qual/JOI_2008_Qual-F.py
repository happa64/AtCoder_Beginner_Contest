# https://atcoder.jp/contests/joi2008yo/submissions/15088499
# F - 船旅
import sys
import heapq

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def dijkstra_heap(s):
        # 始点sから各頂点への最短距離
        d = [f_inf] * n
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

    n, k = map(int, input().split())
    edge = [[] for _ in range(n)]

    for _ in range(k):
        q, *query = map(int, input().split())
        if q == 0:
            a, b = query
            cost = dijkstra_heap(a - 1)
            print(-1 if cost[b - 1] == f_inf else cost[b - 1])
        else:
            c, d, e = query
            edge[c - 1].append([e, d - 1])
            edge[d - 1].append([e, c - 1])


if __name__ == '__main__':
    resolve()
