# https://atcoder.jp/contests/joisc2007/tasks/joisc2007_mall
# mall - ショッピングモール (Mall)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = 10 ** 7 + 1
mod = 10 ** 9 + 7


def resolve():
    W, H = map(int, input().split())
    w, h = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if grid[i][j] == -1:
                grid[i][j] = f_inf

    R = [[0 for _ in range(W + 1)] for _ in range(H + 1)]
    for i in range(H):
        for j in range(W):
            R[i + 1][j + 1] = R[i][j + 1] + R[i + 1][j] - R[i][j] + grid[i][j]

    res = f_inf
    for x1 in range(H + 1):
        x2 = x1 + h
        if x2 >= H:
            continue
        for y1 in range(W + 1):
            y2 = y1 + w
            if y2 >= W:
                continue
            total = R[x2][y2] - R[x1][y2] - R[x2][y1] + R[x1][y1]
            res = min(res, total)
    print(res)


if __name__ == '__main__':
    resolve()
