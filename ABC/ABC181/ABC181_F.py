# https://atcoder.jp/contests/abc181/submissions/17831030
# F - Silver Woods
import sys
from math import hypot

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


def main():
    n = int(input())
    XY = [list(map(int, input().split())) for _ in range(n)]

    S, T = n, n + 1
    edge = []
    for i in range(n):
        x, y = XY[i]
        edge.append((y + 100, i, S))
        edge.append((100 - y, i, T))

    for i in range(n):
        x1, y1 = XY[i]
        for j in range(i + 1, n):
            x2, y2 = XY[j]
            edge.append((hypot(x1 - x2, y1 - y2), i, j))

    edge.sort()
    uf = UnionFind(n + 2)
    for l, i, j in edge:
        uf.union(i, j)
        if uf.same(S, T):
            print(l / 2)
            break


if __name__ == '__main__':
    main()
