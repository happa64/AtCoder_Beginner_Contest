def Bellman_ford(n, start, edge):
    """
    負の重みを持つグラフの単一始点最短路を求める。O(V|E|)
    :param n: グラフの頂点数
    :param start: 始点
    :param edge: グラフの情報。[[(辺の重み、頂点),...],[(辺の重み、頂点),...],...]の形であること
    :return :負閉路がある場合Falseを返し、無い場合は始点から各頂点への最短距離を返す
    """
    f_inf = float("inf")
    dist = [f_inf] * n
    dist[start] = 0
    for _ in range(n):
        update = False
        for v in range(n):
            for d, u in edge[v]:
                if dist[v] != f_inf and dist[v] + d < dist[u]:
                    dist[u] = dist[v] + d
                    update = False
        if not update:
            return dist
    return False
