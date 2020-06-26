# https://atcoder.jp/contests/abc075/submissions/14695031
# C - Bridge
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def dfs(v, remove):
        for u in tree[v]:
            if [u, v] == remove or [v, u] == remove:
                continue
            elif visited[u]:
                continue
            else:
                visited[u] = True
                dfs(u, remove)

    n, m = map(int, input().split())
    edge = []
    tree = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        edge.append([a - 1, b - 1])
        tree[a - 1].append(b - 1)
        tree[b - 1].append(a - 1)

    res = 0
    for remove in edge:
        visited = [False for _ in range(n)]
        visited[0] = True
        dfs(0, remove)
        if not all(visited):
            res += 1
    print(res)


if __name__ == '__main__':
    resolve()
