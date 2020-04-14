# 迷路探索問題（ゴールに到達できるか否か）
from collections import deque

H, W = map(int, input().split())
# スタート地点を定義
sh, sw =
# ゴール地点を定義
gh, gw =
# 迷路の入力
grid = [input() for _ in range(H)]
f_inf = float('inf')
maze = [[f_inf] * W for _ in range(H)]
maze[sh][sw] = 0
# 幅優先探索
que = deque([[sh, sw]])
while que:
    h, w = que.popleft()
    for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        next_h, next_w = h + dh, w + dw
        if next_h < 0 or next_h >= H or next_w < 0 or next_w >= W:
            continue
        elif grid[next_h][next_w] == "#":
            continue
        else:
            if maze[next_h][next_w] > maze[h][w] + 1:
                maze[next_h][next_w] = maze[h][w] + 1
                que.append([next_h, next_w])

print(maze[gy][gx])


# 幅優先探索（最短経路問題）
def bfs(v):
    dist = [f_inf for _ in range(n)]
    dist[v] = 0
    q = deque()
    q.append(v)
    while q:
        u = q.popleft()
        for nv in tree[u]:
            if dist[nv] == f_inf:
                dist[nv] = dist[u] + 1
                q.append(nv)
    for d in dist:
        res[d] += 1
