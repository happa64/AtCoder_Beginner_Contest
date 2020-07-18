# https://atcoder.jp/contests/arc025/submissions/15304536
# B - チョコレート
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(H)]

    R_Black = [[0] * (W + 1) for _ in range(H + 1)]
    R_White = [[0] * (W + 1) for _ in range(H + 1)]
    for i in range(H):
        for j in range(W):
            if (i + j) % 2 == 0:
                R_Black[i + 1][j + 1] = R_Black[i][j + 1] + R_Black[i + 1][j] - R_Black[i][j] + grid[i][j]
                R_White[i + 1][j + 1] = R_White[i][j + 1] + R_White[i + 1][j] - R_White[i][j]
            else:
                R_White[i + 1][j + 1] = R_White[i][j + 1] + R_White[i + 1][j] - R_White[i][j] + grid[i][j]
                R_Black[i + 1][j + 1] = R_Black[i][j + 1] + R_Black[i + 1][j] - R_Black[i][j]

    res = 0
    for x1 in range(H):
        for x2 in range(x1 + 1, H+ 1):
            for y1 in range(W):
                for y2 in range(y1 + 1, W + 1):
                    area = (x2 - x1) * (y2 - y1)
                    Black = R_Black[x2][y2] - R_Black[x1][y2] - R_Black[x2][y1] + R_Black[x1][y1]
                    White = R_White[x2][y2] - R_White[x1][y2] - R_White[x2][y1] + R_White[x1][y1]
                    if Black == White:
                        res = max(res, area)
    print(res)


if __name__ == '__main__':
    resolve()
