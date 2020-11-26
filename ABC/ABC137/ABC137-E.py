# https://atcoder.jp/contests/abc137/submissions/18417495
# E - Coins Respawn
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def dfs(v):
        for _, u in edge[v]:
            if visited[u]:
                continue
            visited[u] = True
            dfs(u)

    n, m, p = map(int, input().split())
    dist = [[-f_inf] * n for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        dist[a - 1][b - 1] = max(dist[a - 1][b - 1], c - p)

    edge = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -f_inf:
                edge[i].append([-dist[i][j], j])

    score = [f_inf] * n
    score[0] = 0
    for _ in range(n):
        update = [False] * n
        for v in range(n):
            for d, u in edge[v]:
                if score[v] != f_inf and score[v] + d < score[u]:
                    score[u] = score[v] + d
                    update[u] = True

    visited = [False] * n
    for i in range(n):
        if visited[i]:
            continue
        if update[i]:
            visited[i] = True
            dfs(i)

    if visited[-1]:
        print(-1)
    else:
        print(max(0, score[-1] * -1))


if __name__ == '__main__':
    resolve()
