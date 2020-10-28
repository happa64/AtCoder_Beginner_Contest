# https://atcoder.jp/contests/tenka1-2013-quala/submissions/17703586
# C - 天下一二三パズル
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7
res = 0


def resolve():
    def dfs(h, w):
        global res
        if w >= W:
            h += 1
            w = 0
        if h >= H:
            res += 1
            return

        prev = grid[h][w]
        for i in range(1, 4):
            if i == 1:
                if (w < 1 or grid[h][w - 1] != 1) and (h < 1 or grid[h - 1][w] != 1):
                    grid[h][w] = 1
                    dfs(h, w + 1)
                    grid[h][w] = prev
            elif i == 2:
                if (w < 1 or grid[h][w - 1] != 2) and (w < 2 or grid[h][w - 2] != 2) and (
                        h < 1 or grid[h - 1][w] != 2) and (h < 2 or grid[h - 2][w] != 2):
                    grid[h][w] = 2
                    dfs(h, w + 1)
                    grid[h][w] = prev
            else:
                if (w < 1 or grid[h][w - 1] != 3) and (w < 2 or grid[h][w - 2] != 3) and (
                        w < 3 or grid[h][w - 3] != 3) and (h < 1 or grid[h - 1][w] != 3) and (
                        h < 2 or grid[h - 2][w] != 3) and (h < 3 or grid[h - 3][w] != 3):
                    grid[h][w] = 3
                    dfs(h, w + 1)
                    grid[h][w] = prev

    W, H = map(int, input().split())
    if H > 12:
        H = 12 + H % 4
    if W > 12:
        W = 12 + W % 4
    grid = [[-1] * W for _ in range(H)]
    dfs(0, 0)
    print(res)


if __name__ == '__main__':
    resolve()
