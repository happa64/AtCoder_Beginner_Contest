# https://atcoder.jp/contests/arc005/submissions/14834940
# C - 器物損壊！高橋君
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    grid = list(list(input()) for _ in range(H))

    for h in range(H):
        for w in range(W):
            if grid[h][w] == "s":
                sh, sw = h, w
            if grid[h][w] == "g":
                gh, gw = h, w

    maze = [[f_inf] * W for _ in range(H)]
    maze[sh][sw] = 0
    que = deque([[sh, sw]])
    while que:
        h, w = que.popleft()
        for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_h, next_w = h + dh, w + dw
            if next_h < 0 or next_h >= H or next_w < 0 or next_w >= W:
                continue
            if grid[next_h][next_w] == "#":
                if maze[next_h][next_w] > maze[h][w] + 1:
                    maze[next_h][next_w] = maze[h][w] + 1
                    que.append([next_h, next_w])
            else:
                if maze[next_h][next_w] > maze[h][w]:
                    maze[next_h][next_w] = maze[h][w]
                    que.appendleft([next_h, next_w])

    print("YES" if maze[gh][gw] <= 2 else "NO")


if __name__ == '__main__':
    resolve()
