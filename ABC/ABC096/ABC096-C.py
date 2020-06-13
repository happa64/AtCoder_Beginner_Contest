# https://atcoder.jp/contests/abc096/submissions/13178545
# C - Grid Repainting 2
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    for h in range(H):
        for w in range(W):
            if S[h][w] == "#":
                for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_h, next_w = h + dh, w + dw
                    if next_h < 0 or next_h >= H or next_w < 0 or next_w >= W:
                        continue
                    elif S[next_h][next_w] == "#":
                        break
                else:
                    print("No")
                    exit()

    print("Yes")


if __name__ == '__main__':
    resolve()
