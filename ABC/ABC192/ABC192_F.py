# https://atcoder.jp/contests/abc192/submissions/20512878
# F - Potion
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, x = map(int, input().split())
    A = list(map(int, input().split()))

    res = f_inf
    for k in range(1, n + 1):
        dp = [[-f_inf] * k for _ in range(k + 1)]
        dp[0][0] = 0
        for a in A:
            next_dp = [[-f_inf] * k for _ in range(k + 1)]
            for j in range(k + 1):
                for l in range(k):
                    now = dp[j][l]
                    next_dp[j][l] = max(next_dp[j][l], now)
                    if j + 1 <= k:
                        next_dp[j + 1][(l + a) % k] = max(next_dp[j + 1][(l + a) % k], now + a)
            dp = next_dp
        res = min(res, (x - dp[k][x % k]) // k)
    print(res)


if __name__ == '__main__':
    resolve()
