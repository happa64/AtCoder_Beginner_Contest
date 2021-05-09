# https://codeforces.com/contest/1519/submission/115767620
# B - The Cake Is a Lie
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def solve():
    n, m, k = map(int, input().split())
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 0
    for x in range(n):
        for y in range(m):
            now = dp[x][y]
            if x + 1 < n:
                dp[x + 1][y] = now + y + 1
            if y + 1 < m:
                dp[x][y + 1] = now + x + 1
    print("YES" if dp[-1][-1] == k else "NO")


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()
