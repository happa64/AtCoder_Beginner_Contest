# https://atcoder.jp/contests/abc141/submissions/14866495
# E - Who Says a Pun?
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    s = input()[::-1]

    res = 0
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                res = max(res, min(j - i, dp[i][j]))

    print(res)


if __name__ == '__main__':
    resolve()
