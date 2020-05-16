# https://atcoder.jp/contests/abc068/submissions/12987221
# C - Cat Snuke and a Voyage
import sys
import heapq

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())

    edge = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        edge[a - 1].append(b - 1)
        edge[b - 1].append(a - 1)

    # 島1から一回の定期便で行ける島に、島Nへの定期便が出ていればOK
    for i in edge[0]:
        if n - 1 in set(edge[i]):
            print("POSSIBLE")
            break
    else:
        print("IMPOSSIBLE")


def resolve2():
    n, m = map(int, input().split())

    edge = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        edge[a - 1].append([1, b - 1])
        edge[b - 1].append([1, a - 1])

    # ダイクストラ法：O(ElogV)
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

    L = dijkstra_heap(n - 1)

    if L[0] <= 2:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")


if __name__ == '__main__':
    resolve()
