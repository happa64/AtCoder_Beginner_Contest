def dijkstra_heap(n, start, edge):
    """
    疎なグラフの単一始点最短路を求める。O(|E|logN) *|E|は辺の数
    :param n: 走査するグラフの頂点数
    :param start: 始点
    :param edge: 重み付き隣接リスト。[cost, node]の形で渡す
    :return: 始点から各頂点への最短距離
    """
    from heapq import heappop, heappush

    f_inf = float("inf")
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


def dijkstra(n, start, edge):
    """
    密なグラフの単一始点最短路を求める。O(N^2)
    :param n: 頂点数
    :param start: 始点
    :param edge: 重み付き隣接リスト。[cost, node]の形で渡す
    :return: 始点から各頂点への最短距離
    """
    f_inf = float("inf")
    res = [f_inf] * n
    res[start] = 0
    used = [False] * n
    for _ in range(n):
        min_dist = f_inf
        min_v = -1
        for v in range(n):
            if not used[v] and res[v] < min_dist:
                min_dist = res[v]
                min_v = v
        if min_v == -1:
            break
        for d, u in edge[min_v]:
            res[u] = min(res[u], res[min_v] + d)
        used[min_v] = True
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
    from heapq import heapify, heappop, heappush

    f_inf = float("inf")
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
            if next_h < 0 or next_h >= H or next_w < 0 or next_w >= W:
                continue
            if grid[next_h][next_w] == "#":
                continue
            if res[next_h][next_w] > grid[next_h][next_w] + res[h][w]:
                res[next_h][next_w] = grid[next_h][next_w] + res[h][w]
                heappush(que, (res[next_h][next_w], next_h, next_w))
    return res
