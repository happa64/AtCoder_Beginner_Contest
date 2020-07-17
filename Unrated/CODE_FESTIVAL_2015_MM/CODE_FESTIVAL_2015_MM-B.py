# https://atcoder.jp/contests/code-festival-2015-morning-middle/submissions/15288096
# B - ヘイホー君と削除
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def LCS(S, T):
    """
    最長共通部分列を求める。dp[-1][-1]が最長共通部分列長である。
    計算量はO(len(S)*len(T))
    :param S: 文字列１
    :param T: 文字列２
    :return: 最長共通部分列
    """
    # 最長共通部分列長を求める
    dp = [[0 for _ in range(len(T) + 1)] for _ in range(len(S) + 1)]
    for i in range(1, len(S) + 1):
        for j in range(1, len(T) + 1):
            x = 1 if S[i - 1] == T[j - 1] else 0
            dp[i][j] = max(dp[i - 1][j - 1] + x, dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]


def resolve():
    n = int(input())
    s = input()

    res = 0
    for i in range(n):
        left = s[:i]
        right = s[i:]
        res = max(res, LCS(left, right) * 2)
    print(n - res)


if __name__ == '__main__':
    resolve()
