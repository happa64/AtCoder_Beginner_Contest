# https://atcoder.jp/contests/abc029/submissions/14091288
# D - 1
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def digit_DP(S):
        L = len(S)
        # dp[決定した桁数][未満フラグ][1が出現する回数]
        dp = [[[0 for _ in range(11)] for _ in range(2)] for _ in range(L + 1)]
        dp[0][0][0] = 1
        for i in range(L):
            for j in range(10):
                dp[i + 1][1][j] += dp[i][1][j] * 9
                dp[i + 1][1][j + 1] += dp[i][1][j]

                if int(S[i]) > 1:
                    dp[i + 1][1][j] += dp[i][0][j] * (int(S[i]) - 1)
                    dp[i + 1][1][j + 1] += dp[i][0][j]
                elif int(S[i]) == 1:
                    dp[i + 1][1][j] += dp[i][0][j]

                if int(S[i]) == 1:
                    dp[i + 1][0][j + 1] = dp[i][0][j]
                else:
                    dp[i + 1][0][j] = dp[i][0][j]

        res = 0
        for j in range(10):
            res += (dp[L][0][j] + dp[L][1][j]) * j

        return res

    n = input()
    print(digit_DP(n))


if __name__ == '__main__':
    resolve()
