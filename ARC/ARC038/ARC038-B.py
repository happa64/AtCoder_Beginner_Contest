# https://atcoder.jp/contests/arc038/submissions/15315786
# B - マス目と駒
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = list(map(int, input().split()))

    def dfs(i, j):
        if i >= H or j >= W or grid[i][j] == '#':
            return True
        if dp[i][j] != -1:
            return dp[i][j]

        res = False
        if not dfs(i + 1, j):
            res = True
        if not dfs(i + 1, j + 1):
            res = True
        if not dfs(i, j + 1):
            res = True
        dp[i][j] = res
        return res

    grid = [list(input()) for _ in range(H)]
    dp = [[-1] * W for _ in range(H)]
    print("First" if dfs(0, 0) else "Second")


if __name__ == '__main__':
    resolve()
