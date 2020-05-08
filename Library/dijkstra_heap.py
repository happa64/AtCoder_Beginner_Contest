import heapq


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

# v:始点から各頂点への距離を計算：O(V)
def dfs(v, p, d):
    depth[v] = d
    for c, u in edge[v]:
        if u == p:
            continue
        dfs(u, v, d + c)

edge = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    edge[a - 1].append([c, b - 1])
    edge[b - 1].append([c, a - 1])
