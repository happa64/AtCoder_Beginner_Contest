# https://atcoder.jp/contests/arc038/submissions/15316015
# B - マス目と駒
import sys
from functools import lru_cache

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = list(map(int, input().split()))

    @lru_cache(maxsize=H * W)
    def dfs(i, j):
        if i >= H or j >= W or grid[i][j] == '#':
            return True

        res = False
        if not dfs(i + 1, j) or not dfs(i + 1, j + 1) or not dfs(i, j + 1):
            res = True
        return res

    grid = [list(input()) for _ in range(H)]
    print("First" if dfs(0, 0) else "Second")


if __name__ == '__main__':
    resolve()
