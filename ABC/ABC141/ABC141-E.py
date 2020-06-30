# https://atcoder.jp/contests/abc141/submissions/14866495
# E - Who Says a Pun?
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    s = input()

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in reversed(range(n)):
        for j in reversed(range(n)):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1

    res = 0
    for i in range(n):
        for j in range(n):
            if i < j:
                now = min(dp[i][j], j - i)
                res = max(res, now)
    print(res)


if __name__ == '__main__':
    resolve()
