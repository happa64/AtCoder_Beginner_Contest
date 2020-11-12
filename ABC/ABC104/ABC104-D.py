# https://atcoder.jp/contests/abc104/submissions/18062576
# D - We Love ABC
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = input()
    n = len(S)

    dp = [[0] * 4 for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(4):
            if S[i] == "?":
                dp[i + 1][j] = (dp[i + 1][j] + dp[i][j] * 3 % mod) % mod
            else:
                dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % mod

        if S[i] == "A" or S[i] == "?":
            dp[i + 1][1] = (dp[i + 1][1] + dp[i][0]) % mod
        if S[i] == "B" or S[i] == "?":
            dp[i + 1][2] = (dp[i + 1][2] + dp[i][1]) % mod
        if S[i] == "C" or S[i] == "?":
            dp[i + 1][3] = (dp[i + 1][3] + dp[i][2]) % mod

    print(dp[-1][-1])


if __name__ == '__main__':
    resolve()
