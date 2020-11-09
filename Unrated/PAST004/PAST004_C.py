# https://atcoder.jp/contests/past202010-open/submissions/18010687
# C - 隣接カウント
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    grid = [list(input().rstrip()) for _ in range(H)]

    D = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            D.append([i, j])

    res = [[""] * W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            cnt = 0
            for dh, dw in D:
                next_h, next_w = h + dh, w + dw
                if next_h < 0 or next_h >= H or next_w < 0 or next_w >= W:
                    continue
                if grid[next_h][next_w] == "#":
                    cnt += 1
            res[h][w] = str(cnt)
    for i in res:
        print("".join(i))


if __name__ == '__main__':
    resolve()
