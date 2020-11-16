# https://atcoder.jp/contests/abc183/submissions/18162656
# F - Confluence
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
        for cost, node1, node2 in edge:
            if not self.same(node1, node2):
                cost_sum += cost
                self.union(node1, node2)
        return cost_sum


def resolve():
    n, q = map(int, input().split())
    C = list(map(int, input().split()))
    query = [list(map(int, input().split())) for _ in range(q)]

    clazz = [defaultdict(int) for _ in range(n)]
    for i in range(n):
        clazz[i][C[i]] = 1

    uf = UnionFind(n)
    for t, *Q in query:
        if t == 1:
            a, b = Q
            a -= 1
            b -= 1
            if not uf.same(a, b):
                a = uf.find(a)
                b = uf.find(b)
                uf.union(a, b)
                if uf.find(a) == a:
                    root = a
                    child = b
                else:
                    root = b
                    child = a
                for k, v in clazz[child].items():
                    clazz[root][k] += v
                    clazz[child][k] = 0
        else:
            x, y = Q
            x -= 1
            root = uf.find(x)
            print(clazz[root][y])


if __name__ == '__main__':
    resolve()
