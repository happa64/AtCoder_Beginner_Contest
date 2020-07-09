# https://atcoder.jp/contests/joi2016yo/submissions/15096909
# C - ロシアの旗 (Russian Flag)
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]

    res = f_inf
    for w in range(1, H - 1):
        cnt_w = W * w
        for i in range(w):
            cnt_w -= grid[i].count("W")
        for b in range(1, H - w):
            cnt_b = W * b
            for i in range(b):
                cnt_b -= grid[w + i].count("B")
            cnt_r = W * (H - w - b)
            for i in range(H - w - b):
                cnt_r -= grid[w + b + i].count("R")
            cnt = cnt_w + cnt_b + cnt_r
            res = min(res, cnt)
    print(res)


if __name__ == '__main__':
    resolve()
