# https://atcoder.jp/contests/past202005-open/submissions/17545829
# M - 行商計画問題
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7
idx = 0


def resolve():
    def bfs(v):
        D = [f_inf] * n
        D[v] = 0
        q = deque([v])
        while q:
            u = q.popleft()
            for v in edge[u]:
                if D[v] == f_inf:
                    D[v] = D[u] + 1
                    q.append(v)
        return D

    n, m = map(int, input().split())
    edge = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        edge[a - 1].append(b - 1)
        edge[b - 1].append(a - 1)
    s = int(input()) - 1
    k = int(input())
    T = list(map(lambda x: int(x) - 1, input().split()))
    T = [s] + T

    dist = [[] for _ in range(k + 1)]
    for i in range(k + 1):
        dist[i] = bfs(T[i])

    dp = [[f_inf] * (k + 1) for _ in range(1 << (k + 1))]
    dp[1][0] = 0
    for S in range(1, 1 << (k + 1)):
        for u in range(k + 1):
            if not (S & (1 << u)):
                continue
            for v in range(k + 1):
                cost = dist[u][T[v]]
                dp[S | (1 << v)][v] = min(dp[S | (1 << v)][v], dp[S][u] + cost)
    print(min(dp[-1]))


if __name__ == '__main__':
    resolve()
