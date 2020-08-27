from heapq import heapify, heappop, heappush


def dijkstra_heap(v, start, edge):
    """
    ダイクストラ法
    :param v: 走査するグラフの頂点数
    :param start: 始点
    :param edge: 重み付き隣接リスト。[cost, node]の形で渡す
    :return: 始点から各頂点への最短距離
    """
    res = [f_inf] * v
    res[start] = 0
    edge_list = []
    for u in edge[start]:
        heappush(edge_list, u)
    while len(edge_list):
        cost, node = heappop(edge_list)
        if dist[node] == f_inf:
            res[node] = cost
            for next_cost, next_node in edge[node]:
                if dist[node] == f_inf:
                    heappush(edge_list, [next_cost + cost, next_node])
    return res


def dijkstra_heap_2d(H, W, grid, sh, sw):
    """
    二次元グリッドにおけるダイクストラ法
    :param H:グリッドの縦の長さ
    :param W: グリッドの横の長さ
    :param grid: グリッドの情報
    :param sh: 始点のy座標
    :param sw: 始点のx座標
    :return: 始点から各頂点への最短距離
    """
    res = [[f_inf] * W for _ in range(H)]
    res[sh][sw] = 0
    que = [(0, sh, sw)]
    heapify(que)
    while que:
        d, h, w = heappop(que)
        if res[h][w] < d:
            continue
        for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_h, next_w = h + dh, w + dw
            if next_h < 0 or next_h >= H or next_w < 0 or next_w >= W or grid[next_h][next_w] == "#":
                continue
            if res[next_h][next_w] > grid[next_h][next_w] + res[h][w]:
                res[next_h][next_w] = grid[next_h][next_w] + res[h][w]
                heappush(que, (res[next_h][next_w], next_h, next_w))
    return res


def dijkstra(s):
    res = [f_inf] * (n + 2)
    res[s] = 0
    checked = [False] * (n + 2)
    while True:
        v = -1
        for k in range(n + 2):
            if (not checked[k]) and (v == -1):
                v = k
            elif (not checked[k]) and res[k] < res[v]:
                v = k
        if v == -1:
            break
        checked[v] = True
        for m in range(n + 2):
            res[m] = min(res[m], res[v] + cost[v][m])
    return res
