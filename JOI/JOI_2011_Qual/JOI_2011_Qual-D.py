# https://atcoder.jp/contests/joi2011yo/submissions/15051400
# D - 1年生 (A First Grader)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    dp = [[0] * 21 for _ in range(n - 1)]
    dp[0][A[0]] = 1
    for i in range(1, n - 1):
        a = A[i]
        for j in range(21):
            if j - a >= 0 and dp[i - 1][j] != 0:
                dp[i][j - a] += dp[i - 1][j]
            if j + a <= 20 and dp[i - 1][j] != 0:
                dp[i][j + a] += dp[i - 1][j]

    print(dp[-1][A[-1]])


if __name__ == '__main__':
    resolve()
