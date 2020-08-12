# https://atcoder.jp/contests/agc046/submissions/15845888
# B - Extension
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 998244353


def resolve():
    A, B, C, D = map(int, input().split())

    dp = [[0] * (D + 1) for _ in range(C + 1)]
    dp[A][B] = 1
    for i in range(A, C + 1):
        for j in range(B, D + 1):
            if i == A and j == B:
                continue
            dp[i][j] = dp[i][j - 1] * i + dp[i - 1][j] * j - dp[i - 1][j - 1] * (i - 1) * (j - 1)
            dp[i][j] %= mod

    print(dp[-1][-1])


if __name__ == '__main__':
    resolve()
