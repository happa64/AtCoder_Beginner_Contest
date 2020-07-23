# https://atcoder.jp/contests/abc067/submissions/15377923
# D - Fennec VS. Snuke
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    edge = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        edge[a - 1].append(b - 1)
        edge[b - 1].append(a - 1)

    dist = [f_inf] * n
    dist[0] = 0
    q = deque([0])
    while q:
        u = q.popleft()
        if u != n - 1:
            for nv in edge[u]:
                if dist[nv] == f_inf:
                    dist[nv] = dist[u] + 1
                    q.append(nv)

    half_dist = (dist[-1] - 1) // 2
    dist2 = [f_inf] * n
    dist2[-1] = 0
    q = deque([n - 1])
    while q:
        u = q.popleft()
        for nv in edge[u]:
            if dist[nv] == f_inf:
                continue
            else:
                if dist2[nv] == f_inf:
                    if dist2[u] + 1 <= half_dist:
                        dist2[nv] = dist2[u] + 1
                        q.append(nv)

    visited = [False] * n
    visited[0] = True
    q = deque([0])
    while q:
        u = q.popleft()
        if u != n - 1:
            for nv in edge[u]:
                if dist2[nv] == f_inf and not visited[nv]:
                    visited[nv] = True
                    q.append(nv)

    fennec = sum(visited)
    snuke = n - fennec
    print("Fennec" if fennec > snuke else "Snuke")


if __name__ == '__main__':
    resolve()
