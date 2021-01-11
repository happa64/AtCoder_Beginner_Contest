# https://atcoder.jp/contests/abc188/submissions/19342071
# E - Peddler
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7
res = -f_inf


def resolve():
    def dfs(init, v):
        global res
        for u in edge[v]:
            if visited[u]:
                continue
            res = max(res, A[u] - init)
            visited[u] = True
            dfs(init, u)

    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    A_ = sorted([[A[i], i] for i in range(n)])
    edge = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        edge[a - 1].append(b - 1)

    visited = [False] * n
    for val, j in A_:
        if visited[j]:
            continue
        dfs(val, j)
    print(res)


if __name__ == '__main__':
    resolve()
