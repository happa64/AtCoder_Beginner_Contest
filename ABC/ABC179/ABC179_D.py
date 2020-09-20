# https://atcoder.jp/contests/abc179/submissions/16902150
# D - Leaping Tak
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 998244353


def resolve():
    n, k = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(k)]

    dp = [0] * (n + 1)
    dp_sum = [0] * (n + 1)
    dp[1] = 1
    dp_sum[1] = 1
    for i in range(2, n + 1):
        for l, r in LR:
            li = max(0, i - r)
            ri = i - l
            if ri < 0:
                continue
            dp[i] += dp_sum[ri] - dp_sum[li - 1]
            dp[i] %= mod
        dp_sum[i] = dp_sum[i - 1] + dp[i]
        dp_sum[i] %= mod
    print(dp[n])


if __name__ == '__main__':
    resolve()
