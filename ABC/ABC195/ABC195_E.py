# https://atcoder.jp/contests/abc195/submissions/20927496
# E - Lucky 7 Battle
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    S = input().rstrip()
    X = input().rstrip()

    dp = [[0] * 7 for _ in range(n + 1)]
    dp[-1][0] = 1
    for i in reversed(range(n)):
        num = pow(10, n - i - 1, 7) * int(S[i]) % 7
        op = X[i]
        for j in range(7):
            if op == "A":
                dp[i][j] = 1 if dp[i + 1][j] == dp[i + 1][(j + num) % 7] == 1 else 0
            else:
                dp[i][j] = 0 if dp[i + 1][j] == dp[i + 1][(j + num) % 7] == 0 else 1
    print("Takahashi" if dp[0][0] else "Aoki")


if __name__ == '__main__':
    solve()
