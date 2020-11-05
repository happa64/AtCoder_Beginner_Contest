# https://atcoder.jp/contests/tenka1-2016-quala/submissions/17889219
# B - PackDrop
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def dfs1(v, p):
        for u in edge[v]:
            if u == p:
                continue
            dfs1(u, v)

        for u in edge[v]:
            if u == p:
                continue
            B[v] = min(B[v], B[u])

    def dfs2(v, p, c):
        B[v] -= c
        for u in edge[v]:
            if u == p:
                continue
            dfs2(u, v, c + B[v])

    n, m = map(int, input().split())
    edge = [[] for _ in range(n)]
    for i in range(1, n):
        p = int(input())
        edge[p].append(i)

    B = [f_inf] * n
    B[0] = 0
    for _ in range(m):
        b, c = map(int, input().split())
        B[b] = c

    dfs1(0, - 1)
    dfs2(0, -1, 0)
    print(sum(B))




if __name__ == '__main__':
    resolve()
