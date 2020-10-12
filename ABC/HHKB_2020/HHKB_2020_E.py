# https://atcoder.jp/contests/hhkb2020/tasks/hhkb2020_e
# E - Lamps
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    grid = tuple(tuple(input().rstrip()) for _ in range(H))

    dot_cnt = 0
    yoko = [[0] * W for _ in range(H)]
    for h in range(H):
        cnt = 0
        for w in range(W):
            if grid[h][w] == "#":
                cnt = 0
            else:
                dot_cnt += 1
                cnt += 1
                yoko[h][w] = cnt
        ma = 0
        for w in reversed(range(W)):
            ma = 0 if grid[h][w] == "#" else max(ma, yoko[h][w])
            yoko[h][w] = ma

    tate = [[0] * W for _ in range(H)]
    for w in range(W):
        cnt = 0
        for h in range(H):
            if grid[h][w] == "#":
                cnt = 0
            else:
                cnt += 1
                tate[h][w] = cnt
        ma = 0
        for h in reversed(range(H)):
            ma = 0 if grid[h][w] == "#" else max(ma, tate[h][w])
            tate[h][w] = ma

    for h in range(H):
        for w in range(W):
            yoko[h][w] += tate[h][w] - 1

    p = [1] * (dot_cnt + 1)
    for i in range(1, dot_cnt + 1):
        p[i] = p[i - 1] * 2 % mod

    res = 0
    for h in range(H):
        for w in range(W):
            if grid[h][w] == ".":
                res += p[-1] - p[dot_cnt - yoko[h][w]]
                res %= mod
    print(res)


if __name__ == '__main__':
    resolve()
