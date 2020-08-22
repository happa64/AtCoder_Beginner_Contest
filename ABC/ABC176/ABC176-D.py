# https://atcoder.jp/contests/abc176/submissions/16122602
# D - Wizard in Maze
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    sh, sw = map(lambda x: int(x) - 1, input().split())
    gh, gw = map(lambda x: int(x) - 1, input().split())
    grid = [list(input().rstrip()) for _ in range(H)]

    maze = [[f_inf] * W for _ in range(H)]
    maze[sh][sw] = 0
    que = deque([[sh, sw]])
    while que:
        h, w = que.popleft()
        for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_h, next_w = h + dh, w + dw
            if next_h < 0 or next_h >= H or next_w < 0 or next_w >= W:
                continue
            if grid[next_h][next_w] == ".":
                if maze[next_h][next_w] > maze[h][w]:
                    maze[next_h][next_w] = maze[h][w]
                    que.appendleft([next_h, next_w])
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                next_h, next_w = h + dh, w + dw
                if next_h < 0 or next_h >= H or next_w < 0 or next_w >= W:
                    continue
                if grid[next_h][next_w] == ".":
                    if maze[next_h][next_w] > maze[h][w] + 1:
                        maze[next_h][next_w] = maze[h][w] + 1
                        que.append([next_h, next_w])
    print(maze[gh][gw] if maze[gh][gw] != f_inf else -1)


if __name__ == '__main__':
    resolve()
