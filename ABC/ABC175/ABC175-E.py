# https://atcoder.jp/contests/abc175/submissions/15997510
# E - Picking Goods
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W, k = map(int, input().split())
    grid = [[0] * W for _ in range(H)]
    for _ in range(k):
        r, c, v = map(int, input().split())
        grid[r - 1][c - 1] = v

    # dp[i][h][w]:h行目のアイテムをi個取得した時の、座標(h,w)における価値の最大値
    dp = [[[0] * W for _ in range(H)] for _ in range(4)]
    dp[1][0][0] = grid[0][0]
    for h in range(H):
        for w in range(W):
            for i in range(4):
                # 下に移動する場合
                if h + 1 < H:
                    # アイテムを取らない
                    dp[0][h + 1][w] = max(dp[0][h + 1][w], dp[i][h][w])
                    # アイテムを取る
                    dp[1][h + 1][w] = max(dp[1][h + 1][w], dp[i][h][w] + grid[h + 1][w])
                # 右に移動する場合
                if w + 1 < W:
                    # アイテムを取らない
                    dp[i][h][w + 1] = max(dp[i][h][w + 1], dp[i][h][w])
                    # アイテムを取る（但し、4個以上所持してはいけない）
                    if i + 1 < 4:
                        dp[i + 1][h][w + 1] = max(dp[i + 1][h][w + 1], dp[i][h][w] + grid[h][w + 1])
    res = 0
    for i in range(4):
        res = max(res, dp[i][-1][-1])
    print(res)


if __name__ == '__main__':
    resolve()
