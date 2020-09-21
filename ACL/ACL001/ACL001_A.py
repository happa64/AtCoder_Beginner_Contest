# https://atcoder.jp/contests/acl1/tasks/acl1_a
# A - Reachable Towns
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
        for cost, node1, node2 in edge:
            if not self.same(node1, node2):
                cost_sum += cost
                self.union(node1, node2)
        return cost_sum


def resolve():
    n = int(input())
    XY = [list(map(int, input().split())) for _ in range(n)]
    XY_sort = sorted([[xy[0], xy[1], i] for i, xy in enumerate(XY)])

    uf = UnionFind(n)
    stack = []
    for x, y, idx in XY_sort:
        mi = y
        mi_idx = idx
        while stack and XY[stack[-1]][1] < y:
            v = stack.pop()
            if mi > XY[v][1]:
                mi = XY[v][1]
                mi_idx = v
            uf.union(idx, v)
        stack.append(mi_idx)

    for i in range(n):
        print(uf.size(i))


if __name__ == '__main__':
    resolve()
