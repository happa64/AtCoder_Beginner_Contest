# https://atcoder.jp/contests/abc010/submissions/16577034
# D - 浮気予防
import sys
from itertools import product
from collections import deque

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


class Dinic:
    def __init__(self, N):
        self.N = N
        self.G = [[] for _ in range(N)]

    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)

    def bfs(self, s, t):
        self.level = [None] * self.N
        self.level[s] = 0
        que = deque([s])
        G = self.G
        while que:
            v = que.popleft()
            next_level = self.level[v] + 1
            for w, cap, _ in G[v]:
                if cap and self.level[w] is None:
                    self.level[w] = next_level
                    que.append(w)
        return self.level[t] is not None

    def dfs(self, v, t, f):
        if v == t:
            return f
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        INF = 10 ** 9 + 7
        G = self.G
        while self.bfs(s, t):
            *self.it, = map(iter, self.G)
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow


def resolve():
    """ 部分点解法（bit全探索）"""

    def dfs(v):
        for u in tree[v]:
            if [v, u] in removed or [u, v] in removed:
                continue
            elif visited[u]:
                continue
            else:
                visited[u] = True
                dfs(u)

    n, g, e = map(int, input().split())
    P = list(map(int, input().split()))
    tree = [[] for _ in range(n)]
    edge = []
    for _ in range(e):
        a, b = map(int, input().split())
        edge.append([a, b])
        tree[a].append(b)
        tree[b].append(a)

    res = f_inf
    for pattern in product([0, 1], repeat=e):
        removed = []
        for i in range(e):
            if pattern[i] == 1:
                removed.append(edge[i])
        visited = [False for _ in range(n)]
        dfs(0)
        cnt = 0
        for p in P:
            if visited[p]:
                cnt += 1
        res = min(res, sum(pattern) + cnt)

    print(res)


def resolve2():
    """満点解法（最大流）"""
    n, g, e = map(int, input().split())
    P = list(map(int, input().split()))
    edge = [list(map(int, input().split())) for _ in range(e)] + [[p, n] for p in P]
    mf = Dinic(n + 1)
    for a, b in edge:
        mf.add_edge(a, b, 1)
        mf.add_edge(b, a, 1)
    res = mf.flow(0, n)
    print(res)


if __name__ == '__main__':
    resolve2()
