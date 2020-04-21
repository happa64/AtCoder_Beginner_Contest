# https://atcoder.jp/contests/abc011/tasks/abc011_4
# D - 大ジャンプ(100点解法）
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, d = map(int, input().split())
    x, y = map(int, input().split())



    # メモ化再帰
    dp = [[[-1 for _ in range(2 * n + 1)] for _ in range(2 * n + 1)] for _ in range(n + 1)]

    def dfs(count, now_x, now_y):
        if count == n:
            return now_x == x and now_y == y
        if dp[count][now_x][now_y] != -1:
            return dp[count][now_x][now_y]

        p = 0
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_x, next_y = now_x + dx, now_y + dy
            p += dfs(count + 1, next_x, next_y)
            dp[count][now_x][now_y] = p
        return p

    res = dfs(0, 0, 0)
    print(res / 4 ** n)


if __name__ == '__main__':
    resolve()
