# https://atcoder.jp/contests/past202010-open/submissions/18010713
# G - 村整備
import sys
from copy import deepcopy
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    grid_init = [list(input().rstrip()) for _ in range(H)]

    res = 0
    for y in range(H):
        for x in range(W):
            if grid_init[y][x] == ".":
                continue
            grid = deepcopy(grid_init)
            grid[y][x] = "."
            visited = [[False] * W for _ in range(H)]
            que = deque([[y, x]])
            while que:
                h, w = que.popleft()
                for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_h, next_w = h + dh, w + dw
                    if next_h < 0 or next_h >= H or next_w < 0 or next_w >= W:
                        continue
                    elif grid[next_h][next_w] == "#":
                        continue
                    elif visited[next_h][next_w]:
                        continue
                    else:
                        visited[next_h][next_w] = True
                        que.append([next_h, next_w])

            flg = True
            for h in range(H):
                for w in range(W):
                    if grid[h][w] == "." and not visited[h][w]:
                        flg = False
            if flg:
                res += 1
    print(res)


if __name__ == '__main__':
    resolve()
