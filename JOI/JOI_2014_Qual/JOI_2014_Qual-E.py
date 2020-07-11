# https://atcoder.jp/contests/joi2014yo/submissions/15130264
# E - タクシー (Taxis)
import sys
from collections import deque
from heapq import heappop, heappush

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    C, R = [], []
    for i in range(n):
        c, r = map(int, input().split())
        C.append(c)
        R.append(r)
    tree = [[] for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        tree[a - 1].append(b - 1)
        tree[b - 1].append(a - 1)

    edge = [[] for _ in range(n)]
    for i in range(n):
        que = deque([i])
        dist = [f_inf] * n
        dist[i] = 0
        while que:
            v = que.popleft()
            if dist[v] == R[i]:
                continue
            for u in tree[v]:
                if dist[u] == f_inf:
                    dist[u] = dist[v] + 1
                    que.append(u)
                    edge[i].append(u)
    del tree

    dist = [f_inf] * n
    dist[0] = 0
    que = [(0, 0)]
    while que:
        d, v = heappop(que)
        if d > dist[v]:
            continue
        if v == n - 1:
            print(d)
            break
        for u in edge[v]:
            if dist[u] > d + C[v]:
                dist[u] = d + C[v]
                heappush(que, (dist[u], u))


if __name__ == '__main__':
    resolve()
