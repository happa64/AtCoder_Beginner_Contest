# https://atcoder.jp/contests/abc207/submissions/23821364
# E - Mod i
import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    A = tuple(map(int, input().split()))
    # Aの累積和
    pre_sum = [0] + list(accumulate(A))
    # dp[i][j]:最後の区切りがiで次がj番目のグループの個数
    dp = [[0] * (n + 5) for _ in range(n + 5)]
    dp[0][1] = 1
    # ds[j][k]:mod jでkのグループの個数
    ds = [[0] * (n + 5) for _ in range(n + 5)]
    ds[1][0] = 1
    for i in range(1, n + 1):
        for j in reversed(range(1, i + 1)):
            # now = 0
            # for k in range(i):
            #     if (pre_sum[i] - pre_sum[k]) % j == 0:
            #         now += dp[k][j]
            now = ds[j][pre_sum[i] % j]
            dp[i][j + 1] = now
            ds[j + 1][pre_sum[i] % (j + 1)] += now
            ds[j + 1][pre_sum[i] % (j + 1)] %= MOD
    res = 0
    for j in range(1, n + 2):
        res += dp[n][j]
        res %= MOD
    print(res)


if __name__ == '__main__':
    solve()
