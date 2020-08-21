# https://atcoder.jp/contests/joi2012yo/submissions/16076877
# D - パスタ (Pasta)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 4


def resolve():
    n, k = map(int, input().split())
    menu = [0] * (n + 1)
    for _ in range(k):
        a, b = map(int, input().split())
        menu[a - 1] = b

    dp = [[[0] * 4 for _ in range(4)] for _ in range(n)]
    # 初日の初期化
    if menu[0] != 0:
        now = menu[0]
        dp[0][0][now] = 1
    else:
        for now in range(1, 4):
            dp[0][0][now] = 1
    # 二日目の初期化
    for prev in range(1, 4):
        if menu[1] != 0:
            now = menu[1]
            dp[1][prev][now] += dp[0][0][prev]
        else:
            for now in range(1, 4):
                dp[1][prev][now] += dp[0][0][prev]
    # 三日目以降
    for i in range(2, n):
        for two_prev in range(1, 4):
            for prev in range(1, 4):
                if menu[i] == 0:
                    for now in range(1, 4):
                        if two_prev == prev == now:
                            continue
                        dp[i][prev][now] += dp[i - 1][two_prev][prev]
                        dp[i][prev][now] %= mod
                else:
                    now = menu[i]
                    if two_prev == prev == now:
                        continue
                    dp[i][prev][now] += dp[i - 1][two_prev][prev]
                    dp[i][prev][now] %= mod

    res = 0
    for i in range(1, 4):
        for j in range(1, 4):
            res += dp[-1][i][j]
            res %= mod
    print(res)


if __name__ == '__main__':
    resolve()
