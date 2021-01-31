# https://atcoder.jp/contests/abc190/submissions/19806018
# E - Magical Ornament
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


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


def resolve():
    n, m = map(int, input().split())
    edge = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        edge[a].append(b)
        edge[b].append(a)
    k = int(input())
    C = list(map(lambda x: int(x) - 1, input().split()))
    dist = [[] for _ in range(k)]
    for i in range(k):
        dist[i] = bfs(C[i], edge)
    dp = [[f_inf] * k for _ in range(1 << k)]
    dp[0][0] = 0
    for S in range(1 << k):
        if S == 0:
            for u in range(k):
                dp[S | (1 << u)][u] = 1
        else:
            for u in range(k):
                if not (S & (1 << u)):
                    continue
                for v in range(k):
                    if S & (1 << v):
                        continue
                    d = dist[u][C[v]]
                    dp[S | (1 << v)][v] = min(dp[S | (1 << v)][v], dp[S][u] + d)
    res = min(dp[-1])
    print(res if res != f_inf else -1)


if __name__ == '__main__':
    resolve()
