# https://atcoder.jp/contests/abc130/submissions/16497228
# E - Common Subsequence
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n + 1):
        for j in range(m + 1):
            if i - 1 >= 0:
                dp[i][j] += dp[i - 1][j]
            if j - 1 >= 0:
                dp[i][j] += dp[i][j - 1]
            if i - 1 >= 0 and j - 1 >= 0:
                dp[i][j] -= dp[i - 1][j - 1]
                if S[i - 1] == T[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
            dp[i][j] %= mod
    print(dp[-1][-1])


if __name__ == '__main__':

    resolve2()
