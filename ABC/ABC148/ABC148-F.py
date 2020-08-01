# https://atcoder.jp/contests/abc148/submissions/15562911
# F - Playing Tag on Tree
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def bfs(start):
        dist = [f_inf] * n
        dist[start] = 0
        que = deque([start])
        while que:
            v = que.popleft()
            for u in edge[v]:
                if dist[u] == f_inf:
                    dist[u] = dist[v] + 1
                    que.append(u)
        return dist

    n, u, v = map(int, input().split())
    edge = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        edge[a - 1].append(b - 1)
        edge[b - 1].append(a - 1)

    distT = bfs(u - 1)
    distA = bfs(v - 1)

    res = 0
    for i in range(n):
        if distT[i] < distA[i]:
            res = max(res, distA[i])
    print(res - 1)


if __name__ == '__main__':
    resolve()
