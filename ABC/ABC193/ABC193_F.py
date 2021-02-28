# https://atcoder.jp/contests/abc193/submissions/20564671
# F - Zebraness
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
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
    n = int(input())
    grid = [list(input().rstrip()) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if (i + j) % 2:
                grid[i][j] = "W" if grid[i][j] == "B" else "B" if grid[i][j] == "W" else "?"

    sv = n * n
    tv = sv + 1
    M = 5
    mf = Dinic(tv + 1)
    tot = 0

    for i in range(n):
        for j in range(n):
            v = i * n + j
            for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                ni, nj = i + di, j + dj
                if ni < 0 or nj < 0 or ni >= n or nj >= n:
                    continue
                nv = ni * n + nj
                mf.add_edge(v, nv, 1)
                if v < nv:
                    tot += 1
            if grid[i][j] == "W":
                mf.add_edge(sv, v, M)
                mf.add_edge(v, tv, 0)
            elif grid[i][j] == "B":
                mf.add_edge(sv, v, 0)
                mf.add_edge(v, tv, M)

    res = tot - mf.flow(sv, tv)
    print(res)


if __name__ == '__main__':
    resolve()
