# https://atcoder.jp/contests/tdpc/submissions/17134910
# B - ゲーム
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    dp = [[0] * (b + 1) for _ in range(a + 1)]
    for i in reversed(range(a + 1)):
        for j in reversed(range(b + 1)):
            if i == a and j == b:
                continue
            if (i + j) % 2 == 0:
                if i == a:
                    dp[i][j] = dp[i][j + 1] + B[j]
                elif j == b:
                    dp[i][j] = dp[i + 1][j] + A[i]
                else:
                    dp[i][j] = max(dp[i + 1][j] + A[i], dp[i][j + 1] + B[j])
            else:
                if i == a:
                    dp[i][j] = dp[i][j + 1]
                elif j == b:
                    dp[i][j] = dp[i + 1][j]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j + 1])
    print(dp[0][0])


if __name__ == '__main__':
    resolve()
