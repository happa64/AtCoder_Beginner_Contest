color = [-1] * n
def dfs(v, graph, cur=0):
    """
    二部グラフ判定
    :param v: 始点
    :param graph: 判定したいグラフ
    :param cur: 塗る色。初期値は0
    :return: 二部グラフであれば真を返す
    """
    color[v] = cur
    for u in edge[v]:
        if color[u] != -1:
            if color[u] == cur:
                return False
            continue
        if not dfs(u, graph, 1 - cur):
            return False
    return True