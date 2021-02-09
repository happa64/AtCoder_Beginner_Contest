# https://atcoder.jp/contests/indeednow-finala-open/submissions/20067734
# C - Optimal Recommendations
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())

    dp = [[[0] * 102 for _ in range(102)] for _ in range(102)]
    for i in range(n):
        a, b, c, w = map(int, input().split())
        dp[a][b][c] = max(dp[a][b][c], w)

    for i in range(101):
        for j in range(101):
            for k in range(101):
                now = dp[i][j][k]
                dp[i + 1][j][k] = max(dp[i + 1][j][k], now)
                dp[i][j + 1][k] = max(dp[i][j + 1][k], now)
                dp[i][j][k + 1] = max(dp[i][j][k + 1], now)
                dp[i + 1][j + 1][k] = max(dp[i + 1][j + 1][k], now)
                dp[i + 1][j][k + 1] = max(dp[i + 1][j][k + 1], now)
                dp[i][j + 1][k + 1] = max(dp[i][j + 1][k + 1], now)
                dp[i + 1][j + 1][k + 1] = max(dp[i + 1][j + 1][k + 1], now)

    for _ in range(m):
        x, y, z = map(int, input().split())
        print(dp[x][y][z])


if __name__ == '__main__':
    resolve()
