# https://atcoder.jp/contests/dp/submissions/19843822
# S - Digit Sum
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    K = input().rstrip()
    D = int(input())
    dp = [[[0] * D for _ in range(len(K) + 1)] for _ in range(2)]
    dp[0][0][0] = 1
    for i in range(len(K)):
        num = int(K[i])
        for j in range(D):
            for k in range(10):
                dp[1][i + 1][(j + k) % D] = (dp[1][i + 1][(j + k) % D] + dp[1][i][j]) % mod
            for k in range(num):
                dp[1][i + 1][(j + k) % D] = (dp[1][i + 1][(j + k) % D] + dp[0][i][j]) % mod
            dp[0][i + 1][(j + num) % D] = (dp[0][i + 1][(j + num) % D] + dp[0][i][j]) % mod
    res = dp[0][-1][0] + dp[1][-1][0] - 1
    print(res % mod)


if __name__ == '__main__':
    resolve()
