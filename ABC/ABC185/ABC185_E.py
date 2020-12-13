# https://atcoder.jp/contests/abc185/submissions/18767095
# E - Sequence Matching
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    dp = [[f_inf] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp[i][j] = min(dp[i][j], max(i, j))
            else:
                x = 0 if A[i - 1] == B[j - 1] else 1
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + x)
    print(dp[-1][-1])


if __name__ == '__main__':
    resolve()
