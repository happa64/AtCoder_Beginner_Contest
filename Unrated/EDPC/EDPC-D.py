# https://atcoder.jp/contests/dp/submissions/13595578
# D - Knapsack 1
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, w = map(int, input().split())
    goods = [list(map(int, input().split())) for _ in range(n)]

    dp = [[0 for _ in range(w + 1)] for _ in range(n + 1)]
    for j in range(1, w + 1):
        for i in range(1, n + 1):
            w, v = goods[i - 1]
            if j - w >= 0:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
            else:
                dp[i][j] = dp[i - 1][j]

    print(dp[-1][-1])


if __name__ == '__main__':
    resolve()
