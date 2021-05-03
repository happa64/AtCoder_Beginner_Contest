# https://atcoder.jp/contests/typical90/submissions/22272008
# 008 - AtCounter（★4）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    S = input().rstrip()
    t = "atcoder"

    dp = [[0] * (n + 1) for _ in range(8)]
    dp[0][0] = 1
    for i in range(n):
        s = S[i]
        for j in range(8):
            if j + 1 <= 7 and s == t[j]:
                dp[j + 1][i + 1] += dp[j][i]
                dp[j + 1][i + 1] %= MOD
            dp[j][i + 1] += dp[j][i]
            dp[j][i + 1] %= MOD
    print(dp[-1][-1] % MOD)


if __name__ == '__main__':
    solve()
