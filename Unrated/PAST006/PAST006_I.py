# https://atcoder.jp/contests/past202104-open/submissions/22052280
# I - 魚釣り
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    H, W = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(H)]

    dp = [[[0] * (H + W + 2) for _ in range(W + 1)] for _ in range(H + 1)]
    for h in range(H):
        for w in range(W):
            a = grid[h][w]
            for i in range(H + W + 1):
                dp[h + 1][w][i] = max(dp[h + 1][w][i], dp[h][w][i])
                dp[h + 1][w][i + 1] = max(dp[h + 1][w][i + 1], dp[h][w][i] + a)
                dp[h][w + 1][i] = max(dp[h][w + 1][i], dp[h][w][i])
                dp[h][w + 1][i + 1] = max(dp[h][w + 1][i + 1], dp[h][w][i] + a)

    res = [0] * (H + W - 1)
    for i in range(1, H + W):
        res[i - 1] = max(dp[H - 1][W][i], dp[H][W - 1][i])
    print(*res, sep="\n")


if __name__ == '__main__':
    solve()
