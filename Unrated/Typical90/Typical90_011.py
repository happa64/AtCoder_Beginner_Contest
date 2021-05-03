# https://atcoder.jp/contests/typical90/submissions/21951151
# 011 - Gravy Jobs（★6）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    jobs = [list(map(int, input().split())) for _ in range(n)]
    jobs.sort(key=lambda x: x[0])
    MAX = jobs[-1][0]

    dp = [[0] * (MAX + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        d, c, s = jobs[i - 1]
        for j in range(MAX + 1):
            dp[i][j] = max(dp[i][j], dp[i - 1][j])
            if j + c <= d and j + c <= MAX:
                dp[i][j + c] = max(dp[i][j + c], dp[i - 1][j] + s)
    print(max(dp[-1]))


if __name__ == '__main__':
    solve()
