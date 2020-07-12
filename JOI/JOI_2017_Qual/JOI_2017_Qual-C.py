# https://atcoder.jp/contests/joi2017yo/submissions/15203675
# C - 休憩スペース (Refreshment Area)
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W, d = map(int, input().split())
    grid = [list(input()) for _ in range(H)]

    res = 0
    for h in range(H):
        cnt = 0
        for w in range(W):
            if grid[h][w] == ".":
                cnt += 1
            else:
                res += max(0, cnt - d + 1)
                cnt = 0
        res += max(0, cnt - d + 1)

    for w in range(W):
        cnt = 0
        for h in range(H):
            if grid[h][w] == ".":
                cnt += 1
            else:
                res += max(0, cnt - d + 1)
                cnt = 0
        res += max(0, cnt - d + 1)

    print(res)


if __name__ == '__main__':
    resolve()
