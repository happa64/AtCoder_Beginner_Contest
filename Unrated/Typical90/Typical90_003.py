# https://atcoder.jp/contests/typical90/submissions/21908009
# 003 - Longest Circular Road（★4）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    def dfs(v, p):
        for u in edge[v]:
            if u == p:
                continue
            dist[u] = dist[v] + 1
            dfs(u, v)

    n = int(input())
    edge = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        edge[a - 1].append(b - 1)
        edge[b - 1].append(a - 1)

    dist = [-1] * n
    dist[0] = 0
    dfs(0, -1)

    ns = dist.index(max(dist))
    dist = [f_inf] * n
    dist[ns] = 0
    dfs(ns, -1)
    res = max(dist) + 1
    print(res)


if __name__ == '__main__':
    solve()
