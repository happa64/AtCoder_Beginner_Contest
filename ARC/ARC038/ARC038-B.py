# https://atcoder.jp/contests/arc038/submissions/16937928
# B - マス目と駒
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def dfs(i, j):
        if i >= H or j >= W or grid[i][j] == '#':
            return True

        if dp[i][j] is not None:
            return dp[i][j]

        res = True if not dfs(i + 1, j) or not dfs(i + 1, j + 1) or not dfs(i, j + 1) else False
        dp[i][j] = res

        return res

    H, W = list(map(int, input().split()))
    grid = [list(input()) for _ in range(H)]
    dp = [[None] * W for _ in range(H)]
    print("First" if dfs(0, 0) else "Second")


if __name__ == '__main__':
    resolve()
