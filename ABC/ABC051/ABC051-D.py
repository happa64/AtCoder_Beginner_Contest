# https://atcoder.jp/contests/abc051/submissions/13667789
# D - Candidates of No Shortest Paths
import sys
import heapq

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    # 隣接リスト
    edge = [[] for _ in range(n)]
    # 辺の情報
    AB = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edge[a - 1].append([c, b - 1])
        edge[b - 1].append([c, a - 1])
        AB.append([c, a - 1, b - 1])

    # ダイクストラ法（最短経路を計算）
    def dijkstra_heap(s):
        d = [f_inf] * n
        used = [True] * n
        d[s] = 0
        used[s] = False
        edgelist = []
        for e in edge[s]:
            heapq.heappush(edgelist, e)
        while len(edgelist):
            minedge = heapq.heappop(edgelist)
            if not used[minedge[1]]:
                continue
            v = minedge[1]
            d[v] = minedge[0]
            used[v] = False
            for e in edge[v]:
                if used[e[1]]:
                    heapq.heappush(edgelist, [e[0] + d[v], e[1]])
        return d

    # (頂点a~頂点b，距離c)の辺が使われるには、(根~aの距離)+c==(根~bの距離)とならなければならない。
    used = set()
    for i in range(n):
        dist = dijkstra_heap(i)
        for d, to, fr in AB:
            if dist[to] + d == dist[fr]:
                used.add((to, fr))

    print(len(AB) - len(used))


if __name__ == '__main__':
    resolve()
