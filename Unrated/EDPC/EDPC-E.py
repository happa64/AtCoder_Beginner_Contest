# https://atcoder.jp/contests/dp/submissions/13596475
# E - Knapsack 2
import sys
import numpy as np

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, W = map(int, input().split())
    goods = [list(map(int, input().split())) for _ in range(n)]

    max_value = 1
    for i in range(n):
        max_value += goods[i][1]

    dp = [[f_inf for _ in range(max_value)] for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 0

    for j in range(1, max_value):
        for i in range(1, n + 1):
            w, v = goods[i - 1]
            if j - v >= 0:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - v] + w)
            else:
                dp[i][j] = dp[i - 1][j]

    res = 0
    for k in range(max_value):
        if dp[-1][k] <= W:
            res = k

    print(res)


def resolve2():
    N, W = map(int, input().split())

    max_v = 0
    dp = np.full(10 ** 5 + 1, f_inf)
    dp[0] = 0
    for _ in range(N):
        w, v = map(int, input().split())
        np.minimum(dp[v:max_v + v + 1], dp[:max_v + 1] + w, out=dp[v:max_v + v + 1])
        max_v += v

    answer = np.where(dp <= W)[0].max()
    print(answer)


if __name__ == '__main__':
    resolve2()
