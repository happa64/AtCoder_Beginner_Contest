# https://atcoder.jp/contests/abc143/submissions/16280585
# E - Travel by Car
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m, l = map(int, input().split())
    cost = [[f_inf] * n for _ in range(n)]
    for i in range(n):
        cost[i][i] = 0
    for _ in range(m):
        a, b, c = map(int, input().split())
        cost[a - 1][b - 1] = c
        cost[b - 1][a - 1] = c

    for k in range(n):
        for i in range(n):
            for j in range(n):
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

    res = [[f_inf] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if cost[i][j] <= l:
                res[i][j] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                res[i][j] = min(res[i][j], res[i][k] + res[k][j])

    q = int(input())
    for _ in range(q):
        s, t = map(int, input().split())
        print(-1 if res[s - 1][t - 1] == f_inf else res[s - 1][t - 1] - 1)


if __name__ == '__main__':
    resolve()
