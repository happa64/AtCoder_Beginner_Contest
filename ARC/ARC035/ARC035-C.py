# https://atcoder.jp/contests/arc035/submissions/16224826
# C - アットコーダー王国の交通事情
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    cost = [[f_inf] * n for _ in range(n)]
    for i in range(n):
        cost[i][i] = 0

    for _ in range(m):
        a, b, c = map(int, input().split())
        cost[a - 1][b - 1] = c
        cost[b - 1][a - 1] = c

    res = 0
    for l in range(n):
        for i in range(n):
            for j in range(i + 1, n):
                cost[i][j] = min(cost[i][j], cost[i][l] + cost[l][j])
                cost[j][i] = cost[i][j]
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            res += cost[i][j]

    k = int(input())
    for _ in range(k):
        x, y, z = map(int, input().split())
        if cost[x - 1][y - 1] <= z:
            print(res)
        else:
            res = 0
            for i in range(n):
                for j in range(i + 1, n):
                    cost[i][j] = min(cost[i][j], cost[i][x - 1] + cost[y - 1][j] + z,
                                     cost[i][y - 1] + cost[x - 1][j] + z)
                    cost[j][i] = cost[i][j]
                    res += cost[i][j]
            print(res)


if __name__ == '__main__':
    resolve()
