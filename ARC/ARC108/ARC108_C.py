# https://atcoder.jp/contests/arc108/submissions/18293382
# C - Keep Graph Connected
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


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
    def dfs(v):
        for u in G[v]:
            if uf.same(u, v):
                continue
            uf.union(u, v)
            c = edge[(min(u, v), max(u, v))]
            if res[v] != c:
                res[u] = c
            else:
                for i in range(1, n + 1):
                    if i != c:
                        res[u] = i
                        break
            dfs(u)

    n, m = map(int, input().split())
    G = [[] for _ in range(n)]
    edge = defaultdict(int)
    for _ in range(m):
        u, v, c = map(int, input().split())
        G[u - 1].append(v - 1)
        G[v - 1].append(u - 1)
        edge[(min(u - 1, v - 1), max(u - 1, v - 1))] = c

    res = [-1] * n
    res[0] = 1
    uf = UnionFind(n)
    dfs(0)

    print(*res, sep="\n")


if __name__ == '__main__':
    resolve()
