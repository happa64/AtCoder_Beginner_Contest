import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n, l = map(int, input().split())
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(n):
        dp[i + 1] += dp[i]
        dp[i + 1] %= MOD
        if i + l <= n:
            dp[i + l] += dp[i]
            dp[i + l] %= MOD
    print(dp[-1])


if __name__ == '__main__':
    solve()
