# https://atcoder.jp/contests/joi2009yo/submissions/14955969
# D - 薄氷渡り
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7
res = 0


def resolve():
    def dfs(h, w, d):
        global res
        res = max(res, d)
        grid[h][w] = 0
        for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_h, next_w = h + dh, w + dw
            if next_h < 0 or next_h >= H or next_w < 0 or next_w >= W or grid[next_h][next_w] == 0:
                continue
            dfs(next_h, next_w, d + 1)
        grid[h][w] = 1

    W = int(input())
    H = int(input())
    grid = [list(map(int, input().split())) for _ in range(H)]

    for y in range(H):
        for x in range(W):
            if grid[y][x] == 1:
                dfs(y, x, 1)
    print(res)


if __name__ == '__main__':
    resolve()
