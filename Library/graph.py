# 無向グラフの作成
# nがノードの数
# mがクエリの数
tree = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)


# 重み付き有向グラフの作成
tree = [[] for _ in range(n)]
for _ in range(m):
    L, R, D = map(int, input().split())
    tree[L - 1].append((R - 1, D))
    tree[R - 1].append((L - 1, -D))
