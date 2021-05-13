# https://codeforces.com/contest/1511/submission/116099439
# D - Min Cost String
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    def dfs(u):
        while edge[u]:
            v = edge[u].pop()
            dfs(v)
        path.append(u)

    n, k = map(int, input().split())

    edge = [[] for _ in range(k)]
    for i in range(k):
        for j in range(k):
            edge[i].append(j)

    path = []
    dfs(0)
    path.pop()

    m = len(path)
    ans = "".join(chr(ord("a") + path[i % m]) for i in range(n))
    print(ans)


if __name__ == '__main__':
    solve()
