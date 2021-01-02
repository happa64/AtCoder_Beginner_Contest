# https://atcoder.jp/contests/abc187/submissions/19152232
# E - Through Path
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def bfs(v):
        dist = [f_inf] * n
        dist[v] = 0
        que = deque([v])
        while que:
            v = que.popleft()
            for u in graph[v]:
                if dist[u] == f_inf:
                    dist[u] = dist[v] + 1
                    que.append(u)
        return dist

    def dfs(v, p, c):
        res[v] += c
        for u in graph[v]:
            if u == p:
                continue
            dfs(u, v, res[v])

    n = int(input())
    graph = [[] for _ in range(n)]
    edge = []
    for _ in range(n - 1):
        a, b = map(lambda x: int(x) - 1, input().split())
        edge.append((a, b))
        graph[a].append(b)
        graph[b].append(a)
    q = int(input())
    query = [list(map(int, input().split())) for _ in range(q)]
    dist = bfs(0)
    res = [0] * n
    for t, e, x in query:
        e -= 1
        a, b = edge[e]
        if t == 1:
            if dist[a] < dist[b]:
                res[0] += x
                res[b] -= x
            else:
                res[a] += x
        else:
            if dist[b] < dist[a]:
                res[0] += x
                res[a] -= x
            else:
                res[b] += x

    dfs(0, -1, 0)
    print(*res, sep="\n")


if __name__ == '__main__':
    resolve()
