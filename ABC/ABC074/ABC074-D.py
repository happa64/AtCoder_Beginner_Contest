# https://atcoder.jp/contests/abc074/submissions/15723395
# D - Restoring Road Network
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    flg = [[True] * n for _ in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if grid[i][k] + grid[k][j] < grid[i][j]:
                    print(-1)
                    exit()
                elif grid[i][k] + grid[k][j] == grid[i][j] and i != k and j != k:
                    flg[i][j] = False

    res = 0
    for i in range(n):
        for j in range(n):
            if flg[i][j]:
                res += grid[i][j]
    print(res // 2)


if __name__ == '__main__':
    resolve()
