def dijkstra(s):
    # 始点sから各頂点への最短距離
    # n:頂点数, cost[u][v]:辺uvのコスト(存在しないときはinf)
    d = [f_inf] * (n + 2)
    used = [False] * (n + 2)
    d[s] = 0

    while True:
        v = -1
        # まだ使われてない頂点の中から最小の距離のものを探す
        for k in range(n + 2):
            if (not used[k]) and (v == -1):
                v = k
            elif (not used[k]) and d[k] < d[v]:
                v = k
        if v == -1:
            break
        used[v] = True

        for m in range(n + 2):
            d[m] = min(d[m], d[v] + cost[v][m])
    return d


import heapq


# ダイクストラ法：O(ElogV)
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


# 二次元グリッドにおけるダイクストラ法
def dijkstra_heap_2d(H, W, grid, sh, sw):
    dist = [[f_inf] * W for _ in range(H)]
    dist[sh][sw] = 0
    que = [(dist[sh][sw], sh, sw)]
    heapq.heapify(que)
    while que:
        d, h, w = heapq.heappop(que)
        if dist[h][w] < d:
            continue
        for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_h, next_w = h + dh, w + dw
            if next_h < 0 or next_h >= H or next_w < 0 or next_w >= W:
                continue
            elif grid[next_h][next_w] == "#":
                continue
            else:
                if dist[next_h][next_w] > grid[next_h][next_w] + dist[h][w]:
                    dist[next_h][next_w] = grid[next_h][next_w] + dist[h][w]
                    heapq.heappush(que, (dist[next_h][next_w], next_h, next_w))
    return dist


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
