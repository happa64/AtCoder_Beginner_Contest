# https://atcoder.jp/contests/past202004-open/submissions/13663739
# H - 1-9 Grid
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]

    # 各数字の座標を辞書に入れつつ、Sを0にGを10にする
    idx = defaultdict(list)
    for h in range(H):
        for w in range(W):
            if A[h][w] == "S":
                A[h][w] = 0
                sh, sw = h, w
            elif A[h][w] == "G":
                A[h][w] = 10
                gh, gw = h, w
            idx[int(A[h][w])].append((h, w))

    # 各座標に最短でたどり着ける距離を計算する、最短距離は|y1-y2|+|x1-x2|である
    dp = [[f_inf] * W for _ in range(H)]
    dp[sh][sw] = 0
    for i in range(10):
        for y, x in idx[i]:
            for ny, nx in idx[i + 1]:
                dp[ny][nx] = min(dp[ny][nx], dp[y][x] + abs(y - ny) + abs(x - nx))

    print(dp[gh][gw] if dp[gh][gw] != f_inf else -1)


if __name__ == '__main__':
    resolve()
