# https://atcoder.jp/contests/abc199/submissions/22262479
# D - RGB Coloring 2
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def dfs1(v, edge, visited, res):
    res.append(v)
    visited[v] = True
    for u in edge[v]:
        if visited[u]:
            continue
        dfs1(u, edge, visited, res)
    return res


def dfs2(i, edge, vertexs, col):
    if i == len(vertexs):
        return 1
    res = 0
    v = vertexs[i]
    for c in range(3):
        ok = True
        for u in edge[v]:
            if col[u] == c:
                ok = False
                break
        if not ok:
            continue
        col[v] = c
        res += dfs2(i + 1, edge, vertexs, col)
        col[v] = -1
    return res


def solve():
    n, m = map(int, input().split())
    edge = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        edge[a].append(b)
        edge[b].append(a)

    ans = 1
    visited = [False] * n
    col = [-1] * n
    for i in range(n):
        if visited[i]:
            continue
        vertexs = dfs1(i, edge, visited, [])
        col[vertexs[0]] = 0
        ans *= 3 * dfs2(1, edge, vertexs, col)
    print(ans)


if __name__ == '__main__':
    solve()