# https://atcoder.jp/contests/typical90/submissions/22689950
# 042 - Multiple of 9（★4）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    k = int(input())

    if k % 9:
        print(0)
        exit()

    dp = [0] * (k + 1)
    dp[0] = 1
    for i in range(k + 1):
        for j in range(1, 10):
            if i + j <= k:
                dp[i + j] += dp[i]
                dp[i + j] %= MOD
    print(dp[-1])


if __name__ == '__main__':
    solve()
