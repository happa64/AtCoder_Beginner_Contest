# https://atcoder.jp/contests/abc014/submissions/18249746
# D - 閉路
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


class LCA:
    def __init__(self, G, root=0):
        self.G = G
        self.root = root
        self.n = len(G)
        self.logn = (self.n - 1).bit_length()
        self.depth = [-1 if i != root else 0 for i in range(self.n)]
        self.parent = [[-1] * self.n for _ in range(self.logn)]
        self.dfs()
        self.doubling()

    def dfs(self):
        que = [self.root]
        while que:
            u = que.pop()
            for v in self.G[u]:
                if self.depth[v] == -1:
                    self.depth[v] = self.depth[u] + 1
                    self.parent[0][v] = u
                    que += [v]

    def doubling(self):
        for i in range(1, self.logn):
            for v in range(self.n):
                if self.parent[i - 1][v] != -1:
                    self.parent[i][v] = self.parent[i - 1][self.parent[i - 1][v]]

    def get_lca(self, u, v):
        if self.depth[v] < self.depth[u]:
            u, v = v, u
        du = self.depth[u]
        dv = self.depth[v]

        for i in range(self.logn):
            if (dv - du) >> i & 1:
                v = self.parent[i][v]
        if u == v:
            return u

        for i in range(self.logn - 1, -1, -1):
            pu, pv = self.parent[i][u], self.parent[i][v]
            if pu != pv:
                u, v = pu, pv
        return self.parent[0][u]

    def get_dist(self, u, v):
        r = self.get_lca(u, v)
        dist = (self.depth[u] - self.depth[r]) + (self.depth[v] - self.depth[r])
        return dist


def resolve():
    n = int(input())
    edge = [[] for _ in range(n)]
    for _ in range(n - 1):
        x, y = map(int, input().split())
        edge[x - 1].append(y - 1)
        edge[y - 1].append(x - 1)
    q = int(input())
    query = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(q)]

    lca = LCA(edge, 0)
    for a, b in query:
        print(lca.get_dist(a, b) + 1)


if __name__ == '__main__':
    resolve()
