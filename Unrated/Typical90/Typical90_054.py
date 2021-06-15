# https://atcoder.jp/contests/typical90/submissions/23170660
# 054 - Takahashi Number（★6）
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def bfs(v, edge):
    n = len(edge)
    dist = [f_inf] * n
    dist[v] = 0
    q = deque([v])
    while q:
        u = q.popleft()
        for v in edge[u]:
            if dist[v] == f_inf:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist


def solve():
    n, m = map(int, input().split())
    edge = [[] for _ in range(n + m)]
    for i in range(m):
        _ = int(input())
        for r in map(lambda x: int(x) - 1, input().split()):
            edge[n + i].append(r)
            edge[r].append(n + i)

    res = bfs(0, edge)
    for i in res[:n]:
        print(-1 if i == f_inf else i // 2)


if __name__ == '__main__':
    solve()
