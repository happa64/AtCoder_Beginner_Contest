# https://atcoder.jp/contests/dp/submissions/13661884
# I - Coins
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    P = list(map(float, input().split()))

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1.0

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i][j] += dp[i - 1][j - 1] * P[i - 1]
            dp[i][j - 1] += dp[i - 1][j - 1] * (1.0 - P[i - 1])

    res = 0
    for i in range(n // 2 + 1, n + 1):
        res += dp[-1][i]

    print(res)


if __name__ == '__main__':
    resolve()
