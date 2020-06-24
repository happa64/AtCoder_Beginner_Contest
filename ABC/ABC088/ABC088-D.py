# https://atcoder.jp/contests/abc088/submissions/14651483
# D - Grid Repainting
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]

    maze = [[f_inf] * W for _ in range(H)]
    maze[0][0] = 0
    que = deque([[0, 0]])
    while que:
        h, w = que.popleft()
        for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_h, next_w = h + dh, w + dw
            if next_h < 0 or next_h >= H or next_w < 0 or next_w >= W or grid[next_h][next_w] == "#":
                continue
            if maze[next_h][next_w] > maze[h][w] + 1:
                maze[next_h][next_w] = maze[h][w] + 1
                que.append([next_h, next_w])

    if maze[H - 1][W - 1] == f_inf:
        print(-1)
        exit()

    mi = maze[H - 1][W - 1] + 1

    cnt = 0
    for h in range(H):
        for w in range(W):
            if grid[h][w] == "#":
                cnt += 1
    res = H * W - cnt - mi
    print(res)


if __name__ == '__main__':
    resolve()
