# https://atcoder.jp/contests/past202104-open/submissions/22052242
# K - 共通クーポン
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    PU = [list(map(int, input().split())) for _ in range(n)]

    dp = [[-f_inf] * 100 for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        p, u = PU[i - 1]
        for j in range(100):
            dp[i][j] = max(dp[i][j], dp[i - 1][j])
            q, r = divmod(j + p, 100)
            d = q * 20
            dp[i][r] = max(dp[i][r], dp[i - 1][j] + u - p + d)
    print(max(dp[-1]))


if __name__ == '__main__':
    solve()
