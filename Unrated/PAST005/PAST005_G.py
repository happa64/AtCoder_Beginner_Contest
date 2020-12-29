# https://atcoder.jp/contests/past202012-open/submissions/19042621
# G - ヘビ
import sys
from copy import deepcopy

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def dfs(y, x):
    global res, flg
    res.append((y, x))
    visited[y][x] = True
    for dy, dx in ([0, 1], [1, 0], [-1, 0], [0, -1]):
        ny, nx = y + dy, x + dx
        if ny < 0 or ny >= H or nx < 0 or nx >= W or visited[ny][nx]:
            continue
        dfs(ny, nx)

    if all([visited[h][w] for h in range(H) for w in range(W)]):
        flg = True
    else:
        visited[y][x] = False
        res.pop()


H, W = map(int, input().split())
S = [list(input().rstrip()) for _ in range(H)]
init = [[True] * W for _ in range(H)]
for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            init[h][w] = False


for h in range(H):
    for w in range(W):
        if S[h][w] != "#":
            continue
        res = []
        visited = deepcopy(init)
        flg = False
        dfs(h, w)
        if flg:
            print(len(res))
            for y, x in res:
                print(y + 1, x + 1)
            break
    else:
        continue
    break
