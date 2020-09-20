# https://atcoder.jp/contests/practice2/submissions/16903034
# D - Maxflow
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
    n, m = map(int, input().split())
    grid = [list(input().rstrip()) for _ in range(n)]

    mf = Dinic(n * m + 2)
    start = n * m
    end = start + 1

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "#":
                continue
            if (i + j) % 2 == 0:
                mf.add_edge(start, i * m + j, 1)
                for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    next_i, next_j = i + di, j + dj
                    if next_i < 0 or next_i >= n or next_j < 0 or next_j >= m:
                        continue
                    if grid[next_i][next_j] == "#":
                        continue
                    mf.add_edge(i * m + j, next_i * m + next_j, 1)
            else:
                mf.add_edge(i * m + j, end, 1)

    res = mf.flow(start, end)

    for y in range(n):
        for x in range(m):
            if grid[y][x] == "#" or (y + x) % 2 or (y * m + x) == start or (y * m + x) == end:
                continue
            for to, cap, _ in mf.G[y * m + x]:
                if cap == 0 and to != start and to != end:
                    next_y, next_x = divmod(to, m)
                    if y + 1 == next_y:
                        grid[y][x] = 'v'
                        grid[next_y][next_x] = '^'
                    elif y == next_y + 1:
                        grid[y][x] = '^'
                        grid[next_y][next_x] = 'v'
                    elif x + 1 == next_x:
                        grid[y][x] = '>'
                        grid[next_y][next_x] = '<'
                    elif x == next_x + 1:
                        grid[y][x] = '<'
                        grid[next_y][next_x] = '>'

    print(res)
    print(*[''.join(ret) for ret in grid], sep="\n")


if __name__ == '__main__':
    resolve()
