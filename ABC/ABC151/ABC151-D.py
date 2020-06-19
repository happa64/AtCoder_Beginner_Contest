# https://atcoder.jp/contests/abc151/submissions/14464283
# D - Maze Master
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]

    res = []
    for sh in range(H):
        for sw in range(W):
            if grid[sh][sw] == "#":
                continue
            maze = [[f_inf] * W for _ in range(H)]
            maze[sh][sw] = 0
            que = deque([[sh, sw]])
            while que:
                h, w = que.popleft()
                for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_h, next_w = h + dh, w + dw
                    if next_h < 0 or next_h >= H or next_w < 0 or next_w >= W or grid[next_h][
                        next_w] == "#":
                        continue
                    if maze[next_h][next_w] > maze[h][w] + 1:
                        maze[next_h][next_w] = maze[h][w] + 1
                        que.append([next_h, next_w])
                        res.append(maze[next_h][next_w])
    print(max(res))


if __name__ == '__main__':
    resolve()
