# https://atcoder.jp/contests/arc027/submissions/16241106
# C - 最高のトッピングにしような
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    """ 愚直解 """
    X, Y = map(int, input().split())
    n = int(input())
    TH = [list(map(int, input().split())) for _ in range(n)]

    dp = [[[0] * (Y + 1) for _ in range(X + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        t, h = TH[i - 1]
        for prev_x in range(X + 1):
            for prev_y in range(Y + 1):
                for now_x in range(1, min(t + 1, X + 1)):
                    now_y = t - now_x
                    if prev_x + now_x < X + 1 and prev_y + now_y < Y + 1:
                        dp[i][prev_x + now_x][prev_y + now_y] = max(dp[i][prev_x + now_x][prev_y + now_y],
                                                            dp[i - 1][prev_x][prev_y] + h)
                dp[i][prev_x][prev_y] = max(dp[i][prev_x][prev_y], dp[i - 1][prev_x][prev_y])
    res = 0
    for i in range(1, n + 1):
        res = max(res, max(dp[i][-1]))
    print(res)


def resolve2():
    """ 想定解法 """
    X, Y = map(int, input().split())
    n = int(input())
    TH = [list(map(int, input().split())) for _ in range(n)]

    dp = [[0] * (X + Y + 1) for _ in range(X + 1)]
    for t, h in TH:
        next_dp = [[0] * (X + Y + 1) for _ in range(X + 1)]
        for i in range(X + 1):
            for j in range(X + Y + 1):
                next_dp[i][j] = max(next_dp[i][j], dp[i][j])
                if i + 1 < X + 1 and j + t < X + Y + 1:
                    next_dp[i + 1][j + t] = max(next_dp[i + 1][j + t], dp[i][j] + h)
        dp = next_dp
    res = 0
    for i in range(X + 1):
        res = max(res, max(dp[i]))
    print(res)


if __name__ == '__main__':
    resolve2()
