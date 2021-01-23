# 迷路探索問題（ゴールに到達できるか否か）
from collections import deque

H, W = map(int, input().split())
sh, sw = map(int, input().split())
gh, gw = map(int, input().split())
grid = tuple(input().rstrip() for _ in range(H))
f_inf = float('inf')
maze = [[f_inf] * W for _ in range(H)]
maze[sh][sw] = 0
que = deque([[sh, sw]])
while que:
    h, w = que.popleft()
    for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        next_h, next_w = h + dh, w + dw
        if next_h < 0 or next_h >= H or next_w < 0 or next_w >= W or grid[next_h][next_w] == "#":
            continue
        if maze[next_h][next_w] > maze[h][w] + 1:
            maze[next_h][next_w] = maze[h][w] + 1
            que.append([next_h, next_w])
print(maze[gh][gw])


# 幅優先探索（最短経路問題）
def bfs(v, edge):
    n = len(edge)
    dist = [f_inf] * n
    dist[v] = 0
    q = deque([v])
    while q:
        u = q.popleft()
        for v in edge[u]:
            if dist[v] == f_inf:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist
