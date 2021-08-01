# https://atcoder.jp/contests/abc212/submissions/24711800
# E - Safety Journey
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 998244353


def solve():
    n, m, k = map(int, input().split())
    edge = tuple(tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m))

    dp = [[0] * n for _ in range(k + 1)]
    dp[0][0] = 1
    for d in range(k):
        tot = 0
        for v in range(n):
            tot = (tot + dp[d][v]) % MOD
        for v in range(n):
            dp[d + 1][v] = (dp[d + 1][v] + tot - dp[d][v]) % MOD
        for u, v in edge:
            dp[d + 1][v] = (dp[d + 1][v] - dp[d][u]) % MOD
            dp[d + 1][u] = (dp[d + 1][u] - dp[d][v]) % MOD
    res = dp[-1][0]
    print(res)


if __name__ == '__main__':
    solve()
