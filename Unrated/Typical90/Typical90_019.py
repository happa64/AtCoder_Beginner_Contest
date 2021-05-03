# https://atcoder.jp/contests/typical90/submissions/22176195
# 019 - Pick Two（★6）
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    A = list(map(int, input().split()))

    dp = [[f_inf] * (2 * n + 1) for _ in range(2 * n + 1)]
    for i in range(2 * n + 1):
        dp[i][i] = 0

    for L in range(2, 2 * n + 1, 2):
        for l in range(2 * n + 1 - L):
            r = l + L
            dp[l][r] = dp[l + 1][r - 1] + abs(A[l] - A[r - 1])
            for k in range(l, r):
                dp[l][r] = min(dp[l][r], dp[l][k] + dp[k][r])
    print(dp[0][-1])


if __name__ == '__main__':
    solve()