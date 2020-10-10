# https://atcoder.jp/contests/hhkb2020/submissions/17291636
# B - Futon
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    grid = list(list(input().rstrip()) for _ in range(H))

    res = 0
    for h in range(H):
        for w in range(W):
            if grid[h][w] == ".":
                for dh, dw in [(0, 1), (1, 0)]:
                    next_h, next_w = h + dh, w + dw
                    if next_h < 0 or next_h >= H or next_w < 0 or next_w >= W:
                        continue
                    elif grid[next_h][next_w] == "#":
                        continue
                    else:
                        res += 1
    print(res)


if __name__ == '__main__':
    resolve()
