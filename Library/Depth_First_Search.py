# グラフ深さ優先探索
def dfs(v, p):
    for u in tree[v]:
        if u == p:
            continue
        elif visited[u]:
            continue
        else:
            # ここで何らかの処理
            dfs(u, v)