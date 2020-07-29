# https://atcoder.jp/contests/agc023/submissions/15519343
# B - Find Symmetries
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    grid = [list(input().rstrip()) for _ in range(n)]

    for i in range(1, n):
        target = [grid[0][(i + j) % n] for j in range(n)]
        if grid[i] != target:
            break
    else:
        print(n ** 2)
        exit()

    res = 0
    for a in range(n):
        grid2 = [[""] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                grid2[i][j] = grid[(i + a) % n][j]
        for i in range(n):
            for j in range(n):
                if grid2[i][j] != grid2[j][i]:
                    break
            else:
                continue
            break
        else:
            res += 1
    print(res * n)


if __name__ == '__main__':
    resolve()
