# https://atcoder.jp/contests/past202010-open/submissions/18841521
# M - 筆塗り
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


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


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        """xの親を返す"""
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        """yをxの根に繋ぐ（マージテク有）"""
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        """xとyが同じ連結成分か判別する"""
        return self.find(x) == self.find(y)

    def size(self, x):
        """xの連結成分の大きさを返す"""
        return -self.parents[self.find(x)]

    def kruskal(self, edge):
        """
        :param edge: edge = [(コスト, 頂点1, 頂点2),...]の形で重み付き隣接リストを渡して下さい
        :return: 最小全域木のコストの和
        """
        edge.sort()
        cost_sum = 0
        for cost, node1, node2 in edge:
            if not self.same(node1, node2):
                cost_sum += cost
                self.union(node1, node2)
        return cost_sum


def resolve():
    def dfs(x, target, col):
        global res
        que = deque([x])
        while que:
            v = que.pop()
            if v == target:
                break
            for _, u in graph[v]:
                if dist[v] < dist[u]:
                    continue
                idx = edge[min(u, v), max(u, v)]
                if not res[idx]:
                    res[idx] = col
                    prev = root[uf.find(u)]
                    uf.union(u, v)
                    root[uf.find(u)] = u if dist[prev] > dist[u] else prev
                    que.append(u)
                else:
                    u = root[uf.find(u)]
                    if dist[u] <= dist[target]:
                        break
                    que.append(u)

    lca = LowestCommonAncestor(graph)
    uf = UnionFind(n)
    dist = lca.dist
    root = list(range(n))
    for u, v, c in query:
        u, v = u - 1, v - 1
        anc = lca.get_lca(u, v)
        dfs(u, anc, c)
        dfs(v, anc, c)


if __name__ == '__main__':
    n, q = map(int, input().split())
    graph = [[] for _ in range(n)]
    edge = defaultdict(int)
    for i in range(n - 1):
        a, b = map(lambda x: int(x) - 1, input().split())
        edge[(min(a, b), max(a, b))] = i
        graph[a].append([1, b])
        graph[b].append([1, a])
    query = [list(map(int, input().split())) for _ in range(q)][::-1]
    res = [0] * (n - 1)
    resolve()
    print(*res, sep="\n")
