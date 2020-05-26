# https://atcoder.jp/contests/dp/submissions/13594958
# C - Vacation
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    ABC = [list(map(int, input().split())) for _ in range(n)]

    dp = [[0 for _ in range(3)] for _ in range(n)]
    dp[0][0] = ABC[0][0]
    dp[0][1] = ABC[0][1]
    dp[0][2] = ABC[0][2]

    for i in range(1, n):
        a = ABC[i][0]
        b = ABC[i][1]
        c = ABC[i][2]

        dp[i][0] = max(dp[i][0], dp[i - 1][1] + a, dp[i - 1][2] + a)
        dp[i][1] = max(dp[i][1], dp[i - 1][0] + b, dp[i - 1][2] + b)
        dp[i][2] = max(dp[i][2], dp[i - 1][0] + c, dp[i - 1][1] + c)

    print(max(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2]))


if __name__ == '__main__':
    resolve()
