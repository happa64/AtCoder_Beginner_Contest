# https://atcoder.jp/contests/abc169/submissions/16260280
# F - Knapsack for All Subsets
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 998244353


def resolve():
    """ 愚直解 """
    dp = [[0] * (s + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        a = A[i - 1]
        for prev in range(i):
            for j in range(s + 1):
                dp[i][j] += dp[prev][j]
                if a + j > s:
                    continue
                dp[i][a + j] += dp[prev][j]
                dp[i][a + j] %= mod
    print(dp)
    res = 0
    for i in range(1, n + 1):
        res += dp[i][-1]
        res %= mod
    print(res)


def resolve2():
    """ DP + 累積和 """
    dp = [[0] * (s + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    cnt_num = [0] * (s + 1)
    cnt_num[0] = 1
    res = 0
    for i in range(1, n + 1):
        a = A[i - 1]
        for j in range(s + 1):
            dp[i][j] += cnt_num[j]
            dp[i][j] %= mod
            if a + j > s:
                continue
            dp[i][a + j] += cnt_num[j]
            dp[i][a + j] %= mod
        for k in range(s + 1):
            cnt_num[k] = cnt_num[k] + dp[i][k]
            cnt_num[k] %= mod
        res += dp[i][-1]
        res %= mod
    print(res)


if __name__ == '__main__':
    n, s = map(int, input().split())
    A = list(map(int, input().split()))
    resolve2()
