# https://atcoder.jp/contests/abc017/submissions/20242833
# D - サプリメント
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    F = [int(input()) for _ in range(n)]

    dp = [0] * (n + 1)
    dp_sum = [0] * (n + 2)
    dp[0] = dp_sum[1] = 1
    last = [-1] * m
    limit = 0

    for i in range(1, n + 1):
        f = last[F[i - 1] - 1]
        last[F[i - 1] - 1] = i
        if f != -1:
            limit = max(limit, f)
        dp[i] += dp_sum[i] - dp_sum[limit]
        dp[i] %= mod
        dp_sum[i + 1] = dp_sum[i] + dp[i]
        dp_sum[i + 1] %= mod
    print(dp[-1])


if __name__ == '__main__':

    resolve()
