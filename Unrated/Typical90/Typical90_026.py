# https://atcoder.jp/contests/typical90/submissions/22167028
# 026 - Independent Set on a Tree（★4）
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    def dfs(v=0, c=0):
        col[v] = c
        for u in edge[v]:
            if col[u] != -1:
                continue
            dfs(u, c ^ 1)

    n = int(input())
    edge = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(lambda x: int(x) - 1, input().split())
        edge[a].append(b)
        edge[b].append(a)

    col = [-1] * n
    dfs()
    black = [i + 1 for i in range(n) if not col[i]]
    white = [i + 1 for i in range(n) if col[i]]
    if len(black) >= n // 2:
        print(*black[:n // 2], sep="\n")
    else:
        print(*white[:n // 2], sep="\n")


if __name__ == '__main__':
    solve()