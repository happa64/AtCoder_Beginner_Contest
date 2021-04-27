# https://atcoder.jp/contests/past202104-open/submissions/22113043
# O - 最短距離クエリ
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [-1] * n
        self.wei = [0] * n

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            y = self.find(self.par[x])
            self.wei[x] += self.wei[self.par[x]]
            self.par[x] = y
            return y

    def union(self, x, y, w=0):
        w += self.weight(x) - self.weight(y)
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.par[x] > self.par[y]:
            x, y = y, x
            w *= -1
        self.par[x] += self.par[y]
        self.par[y] = x
        self.wei[y] = w
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.par[self.find(x)]

    def weight(self, x):
        self.find(x)
        return self.wei[x]

    def diff(self, x, y):
        return self.weight(y) - self.weight(x)

    def kruskal(self, edge):
        edge.sort()
        cost_sum = 0
        for cost, node1, node2 in edge:
            if not self.same(node1, node2):
                cost_sum += cost
                self.union(node1, node2)
        return cost_sum


class LowestCommonAncestor:
    """木のLCAを求める。構築：O(NlogN),クエリ：O(logN)"""

    def __init__(self, G, root=0):
        """
        :param G: 木の隣接リスト。[(コスト,頂点),(コスト,頂点)…]の形で渡す
        :param root: 木の根
        """
        self.G = G
        self.root = root
        self.n = len(G)
        self.logn = (self.n - 1).bit_length()
        self.dist = [0] * self.n  # dist[v]:根からvの距離
        self.depth = [-1 if i != root else 0 for i in range(self.n)]  # depth[v]:頂点vの深さ
        self.parent = [[-1] * self.n for _ in range(self.logn)]  # parent[k][v]:頂点vの2^k先の親
        self.dfs()
        self.doubling()

    def dfs(self):
        que = [self.root]
        while que:
            u = que.pop()
            for cost, v in self.G[u]:
                if self.depth[v] == -1:
                    self.dist[v] = self.dist[u] + cost
                    self.depth[v] = self.depth[u] + 1
                    self.parent[0][v] = u
                    que += [v]

    def doubling(self):
        for i in range(1, self.logn):
            for v in range(self.n):
                if self.parent[i - 1][v] != -1:
                    self.parent[i][v] = self.parent[i - 1][self.parent[i - 1][v]]

    def get_lca(self, u, v):
        """uとvのLCAをO(logN)で求める"""
        if self.depth[v] < self.depth[u]:
            u, v = v, u
        # LCAまでの距離を同じにする
        du, dv = self.depth[u], self.depth[v]
        for i in range(self.logn):
            if (dv - du) >> i & 1:
                v = self.parent[i][v]
        # 二分探索でLCAを求める
        if u == v:
            return u
        for i in range(self.logn - 1, -1, -1):
            pu, pv = self.parent[i][u], self.parent[i][v]
            if pu != pv:
                u, v = pu, pv
        return self.parent[0][u]

    def get_dist(self, u, v):
        """uとvの距離をO(logN)で求める"""
        r = self.get_lca(u, v)
        return (self.dist[u] - self.dist[r]) + (self.dist[v] - self.dist[r])


def solve():
    n, m = map(int, input().split())
    other_edge = set()
    vertex = []
    tree = [[] for _ in range(n)]
    uf = UnionFind(n)
    for _ in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        if not uf.same(a, b):
            tree[a].append([1, b])
            tree[b].append([1, a])
            uf.union(a, b)
        else:
            other_edge.add((a, b))
            vertex.extend((a, b))

    lca = LowestCommonAncestor(tree)

    L = len(vertex)
    dist = [[f_inf] * L for _ in range(L)]
    for i, u in enumerate(vertex):
        for j, v in enumerate(vertex):
            if i == j:
                dist[i][j] = 0
                continue
            if (u, v) in other_edge or (v, u) in other_edge:
                dist[i][j] = 1
            else:
                dist[i][j] = lca.get_dist(u, v)

    for k in range(L):
        for i in range(L):
            for j in range(L):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    q = int(input())
    for _ in range(q):
        u, v = map(lambda x: int(x) - 1, input().split())
        res = lca.get_dist(u, v)
        dist_u = [lca.get_dist(u, x) for x in vertex]
        dist_v = [lca.get_dist(v, x) for x in vertex]
        for i in range(L):
            for j in range(L):
                if i == j:
                    continue
                d = dist[i][j] + dist_u[i] + dist_v[j]
                res = min(res, d)
        print(res)


if __name__ == '__main__':
    solve()
