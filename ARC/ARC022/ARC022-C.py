# https://atcoder.jp/contests/arc022/submissions/16501347
# C - ロミオとジュリエット
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
        q = deque()
        q.append(v)
        while q:
            u = q.popleft()
            for nv in edge[u]:
                if dist[nv] == f_inf:
                    dist[nv] = dist[u] + 1
                    q.append(nv)
        return dist

    n = int(input())
    edge = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        edge[a - 1].append(b - 1)
        edge[b - 1].append(a - 1)

    dist1 = bfs(0)
    r = dist1.index(max(dist1))
    dist2 = bfs(r)
    j = dist2.index(max(dist2))
    print(r + 1, j + 1)


if __name__ == '__main__':
    resolve()
