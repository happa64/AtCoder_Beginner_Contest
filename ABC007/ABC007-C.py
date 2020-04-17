# https://atcoder.jp/contests/abc007/tasks/abc007_3
# C - 幅優先探索
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    R, C = map(int, input().split())
    sx, sy = map(int, input().split())
    gx, gy = map(int, input().split())
    grid = [list(input()) for _ in range(R)]
    maze = [[f_inf for _ in range(C)] for _ in range(R)]
    maze[sy - 1][sx - 1] = 0
    que = deque([[sy - 1, sx - 1]])
    while que:
        y, x = que.popleft()
        for dy, dx in ((0, -1), (0, 1), (1, 0), (-1, 0)):
            next_x, next_y = x + dx, y + dy
            if grid[next_y][next_x] == "#":
                continue
            else:
                if maze[next_y][next_x] > maze[y][x] + 1:
                    maze[next_y][next_x] = maze[y][x] + 1
                    que.append([next_y, next_x])

    print(maze[gx - 1][gy - 1])


if __name__ == '__main__':
    resolve()
