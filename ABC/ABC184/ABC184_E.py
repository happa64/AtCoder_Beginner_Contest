# https://atcoder.jp/contests/abc184/submissions/18342700
# E - Third Avenue
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    grid = [list(input().rstrip()) for _ in range(H)]

    TP = [[] for _ in range(26)]
    for h in range(H):
        for w in range(W):
            if grid[h][w] == "S":
                sh, sw = h, w
            elif grid[h][w] == "G":
                gh, gw = h, w
            elif grid[h][w] == "." or grid[h][w] == "#":
                continue
            else:
                idx = ord(grid[h][w]) - ord("a")
                TP[idx].append((h, w))
    used = set()
    que = deque([[sh, sw]])
    maze = [[f_inf] * W for _ in range(H)]
    maze[sh][sw] = 0
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
                    if grid[next_h][next_w] != ".":
                        idx = ord(grid[next_h][next_w]) - ord("a")
                        if idx not in used:
                            used.add(idx)
                            for tp_h, tp_w in TP[idx]:
                                if maze[tp_h][tp_w] > maze[next_h][next_w] + 1:
                                    maze[tp_h][tp_w] = maze[next_h][next_w] + 1
                                    que.append([tp_h, tp_w])
    print(maze[gh][gw] if maze[gh][gw] != f_inf else -1)


if __name__ == '__main__':
    resolve()
