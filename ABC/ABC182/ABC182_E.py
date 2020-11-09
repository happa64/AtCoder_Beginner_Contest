# https://atcoder.jp/contests/abc182/submissions/17978164
# E - Akari
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W, n, m = map(int, input().split())
    grid = [["."] * W for _ in range(H)]
    AB = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(n)]
    CD = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

    for a, b in AB:
        grid[a][b] = "x"

    for c, d in CD:
        grid[c][d] = "#"

    check = [[False] * W for _ in range(H)]
    for h in range(H):
        flg = False
        for w in range(W):
            if grid[h][w] == "x":
                flg = True
            if grid[h][w] == "#":
                flg = False
            if flg:
                check[h][w] = True
        for w in reversed(range(W)):
            if grid[h][w] == "x":
                flg = True
            if grid[h][w] == "#":
                flg = False
            if flg:
                check[h][w] = True

    for w in range(W):
        flg = False
        for h in range(H):
            if grid[h][w] == "x":
                flg = True
            if grid[h][w] == "#":
                flg = False
            if flg:
                check[h][w] = True
        for h in reversed(range(H)):
            if grid[h][w] == "x":
                flg = True
            if grid[h][w] == "#":
                flg = False
            if flg:
                check[h][w] = True

    res = 0
    for h in range(H):
        for w in range(W):
            if check[h][w]:
                res += 1
    print(res)


if __name__ == '__main__':
    resolve()
