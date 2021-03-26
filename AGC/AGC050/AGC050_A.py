# https://atcoder.jp/contests/agc050/submissions/21263578
# A - AtCoder Jumper
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    def debug():
        cost = [[f_inf] * n for _ in range(n)]
        for i in range(n):
            cost[i][i] = 0
        for i in range(n):
            for j in edge[i]:
                cost[i][j - 1] = 1

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

        ma = max(max(cost[i]) for i in range(n))
        return ma

    n = int(input())
    edge = [[] for _ in range(n)]
    for i in range(n):
        t1 = ((i + 1) * 2 % n)
        t2 = ((i + 1) * 2 + 1) % n
        edge[i].append(t1 if t1 else n)
        edge[i].append(t2 if t2 else n)

    for i in edge:
        print(*i)


if __name__ == '__main__':
    solve()
