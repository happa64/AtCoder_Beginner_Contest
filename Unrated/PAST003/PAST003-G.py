# https://atcoder.jp/contests/past202005/submissions/13520421
# G - グリッド金移動
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, x, y = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(n)]
    grid = [["." for _ in range(-250, 250)] for _ in range(-250, 250)]

    sh, sw = 201, 201
    gh, gw = y + sh, x + sw
    for x1, y1 in XY:
        grid[y1 + sh][x1 + sw] = "#"

    maze = [[f_inf for _ in range(-250, 250)] for _ in range(-250, 250)]
    maze[sh][sw] = 0
    # 幅優先探索
    que = deque([[sh, sw]])
    while que:
        h, w = que.popleft()
        for dh, dw in ((1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 0)):
            next_h, next_w = h + dh, w + dw
            if next_h < 0 or next_h >= 500 or next_w < 0 or next_w >= 500:
                continue
            if grid[next_h][next_w] == "#":
                continue
            else:
                if maze[next_h][next_w] > maze[h][w] + 1:
                    maze[next_h][next_w] = maze[h][w] + 1
                    que.append([next_h, next_w])

    print(maze[gh][gw] if maze[gh][gw] != f_inf else -1)


if __name__ == '__main__':
    resolve()
