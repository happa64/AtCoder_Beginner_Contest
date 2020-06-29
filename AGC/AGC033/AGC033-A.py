# https://atcoder.jp/contests/agc033/submissions/14834133
# A - Darker and Darker
import sys
from collections import deque
sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    grid = list(list(input()) for _ in range(H))

    que = deque([])
    maze = [[f_inf] * W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if grid[h][w] == "#":
                que.append([h, w])
                maze[h][w] = 0

    while que:
        h, w = que.popleft()
        for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_h, next_w = h + dh, w + dw
            if next_h < 0 or next_h >= H or next_w < 0 or next_w >= W:
                continue
            if maze[next_h][next_w] > maze[h][w] + 1:
                maze[next_h][next_w] = maze[h][w] + 1
                que.append([next_h, next_w])

    res = 0
    for h in range(H):
        for w in range(W):
            res = max(res, maze[h][w])
    print(res)


if __name__ == '__main__':
    resolve()
