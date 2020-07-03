# https://atcoder.jp/contests/cf16-final/submissions/14915239
# C - Interpretation
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def dfs(v):
        for u in edge[v]:
            if visited[u]:
                continue
            else:
                visited[u] = True
                dfs(u)

    n, m = map(int, input().split())
    edge = [[] for _ in range(n + m)]
    for i in range(n):
        _, *L = map(int, input().split())
        for l in L:
            edge[i].append(n + l - 1)
            edge[n + l - 1].append(i)

    visited = [False] * (n + m)
    dfs(0)
    for i in range(n):
        if not visited[i]:
            print("NO")
            break
    else:
        print("YES")


if __name__ == '__main__':
    resolve()
