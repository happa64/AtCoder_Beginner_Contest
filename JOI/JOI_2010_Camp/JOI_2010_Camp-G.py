# https://atcoder.jp/contests/joisc2010/submissions/15121611
# finals - 本選会場 (Finals)
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        """
        親が同じか判別する
        """
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        """
        yをxの根に繋ぐ
        """
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        """
        xとyが同じ連結成分か判別する
        """
        return self.find(x) == self.find(y)

    def size(self, x):
        """
        xの連結成分の大きさを返す
        """
        return -self.parents[self.find(x)]

    def kruskal(self, edge):
        """
        :param edge: edge = [(コスト, 頂点1, 頂点2),...]の形で重み付き隣接リストを渡して下さい
        :return: 最小全域木のコストの和
        """
        edge.sort()
        cost_sum = 0
        used = []
        for cost, node1, node2 in edge:
            if not self.same(node1, node2):
                cost_sum += cost
                self.union(node1, node2)
                used.append([cost, node1, node2])
        return [cost_sum, used]


def resolve():
    n, m, k = map(int, input().split())
    edge = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edge.append([c, a - 1, b - 1])

    uf = UnionFind(n)
    res, used_edge = uf.kruskal(edge)

    used_edge.sort(reverse=True)
    for i in range(k - 1):
        res -= used_edge[i][0]
    print(res)


if __name__ == '__main__':
    resolve()
