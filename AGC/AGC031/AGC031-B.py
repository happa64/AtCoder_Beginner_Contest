# https://atcoder.jp/contests/agc031/submissions/15327890
# B - Reversi
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    C = list(int(input()) for _ in range(n))
    MAX_C = max(C)

    dp = [0] * (n + 1)
    dp[0] = 1
    dp2 = [-1] * (MAX_C + 1)
    for i in range(n):
        c = C[i]
        if dp2[c] >= 0 and dp2[c] < i - 1:
            dp[i + 1] = dp[i] + dp[dp2[c] + 1]
        else:
            dp[i + 1] = dp[i]
        dp[i + 1] %= mod
        dp2[c] = i

    print(dp[-1] % mod)


if __name__ == '__main__':
    resolve()
