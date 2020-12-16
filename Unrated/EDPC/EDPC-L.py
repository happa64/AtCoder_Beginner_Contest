# https://atcoder.jp/contests/dp/submissions/18805610
# L - Deque
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for length in range(1, n + 1):
        i = 0
        while i + length <= n:
            j = i + length
            if (n - length) % 2 == 0:
                dp[i][j] = max(dp[i + 1][j] + A[i], dp[i][j - 1] + A[j - 1])
            else:
                dp[i][j] = min(dp[i + 1][j] - A[i], dp[i][j - 1] - A[j - 1])
            i += 1

    print(dp[0][-1])


if __name__ == '__main__':
    resolve()
