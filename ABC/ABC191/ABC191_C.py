# https://atcoder.jp/contests/abc191/submissions/20003816
# C - Digital Graffiti
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    grid = tuple(input().rstrip() for _ in range(H))

    res = 0
    flg = 0
    for h in range(H):
        for w in range(W):
            if not flg and grid[h][w] == "#":
                res += (grid[h - 1][w] == ".") + (grid[h + 1][w] == ".")
                flg ^= 1
            elif flg and grid[h][w] == ".":
                res += (grid[h - 1][w] == "#") + (grid[h + 1][w] == "#")
                flg ^= 1

    flg = 0
    for h in reversed(range(H)):
        for w in range(W):
            if not flg and grid[h][w] == "#":
                res += (grid[h - 1][w] == ".") + (grid[h + 1][w] == ".")
                flg ^= 1
            elif flg and grid[h][w] == ".":
                res += (grid[h - 1][w] == "#") + (grid[h + 1][w] == "#")
                flg ^= 1

    flg = 0
    for w in range(W):
        for h in range(H):
            if not flg and grid[h][w] == "#":
                res += (grid[h][w - 1] == ".") + (grid[h][w + 1] == ".")
                flg ^= 1
            elif flg and grid[h][w] == ".":
                res += (grid[h][w - 1] == "#") + (grid[h][w + 1] == "#")
                flg ^= 1

    flg = 0
    for w in range(W):
        for h in range(H):
            if not flg and grid[h][w] == "#":
                res += (grid[h][w - 1] == ".") + (grid[h][w + 1] == ".")
                flg ^= 1
            elif flg and grid[h][w] == ".":
                res += (grid[h][w - 1] == "#") + (grid[h][w + 1] == "#")
                flg ^= 1
    print(res // 2)


if __name__ == '__main__':
    resolve()
