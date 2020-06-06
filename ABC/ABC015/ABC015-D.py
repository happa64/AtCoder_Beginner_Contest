# https://atcoder.jp/contests/abc015/submissions/14048732
# D - 高橋くんの苦悩
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    w = int(input())
    n, k = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(n)]

    # dp[i][j][l]:i枚目まで見た時、j枚まで使用でき、かつ幅lまで貼り付けられる時の、重要度の最大値
    dp = [[[0] * (w + 1) for _ in range(k + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        a, b = AB[i - 1]
        for j in range(1, k + 1):
            for l in range(1, w + 1):
                if l - a >= 0:
                    dp[i][j][l] = max(dp[i - 1][j][l], dp[i - 1][j - 1][l - a] + b)
                else:
                    dp[i][j][l] = max(dp[i][j][l], dp[i - 1][j][l])

    print(dp[-1][k][-1])


if __name__ == '__main__':
    resolve()
