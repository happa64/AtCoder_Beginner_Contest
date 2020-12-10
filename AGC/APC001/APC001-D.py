# https://atcoder.jp/contests/apc001/submissions/18669843
# D - Forest
import sys
from heapq import *

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
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    uf = UnionFind(n)
    for _ in range(m):
        x, y = map(int, input().split())
        if not uf.same(x, y):
            uf.union(x, y)

    cost_list = [[] for _ in range(n)]
    for i in range(n):
        root = uf.find(i)
        heappush(cost_list[root], A[i])

    rest_tree = []
    for i in range(n):
        if cost_list[i]:
            heappush(rest_tree, [-len(cost_list[i]), i])

    rest_node, root = heappop(rest_tree)
    rest_node *= -1
    res = 0
    while rest_tree:
        if not rest_node:
            print("Impossible")
            exit()
        _, nxt = heappop(rest_tree)
        c1 = heappop(cost_list[root])
        c2 = heappop(cost_list[nxt])
        res += c1 + c2
        while cost_list[nxt]:
            heappush(cost_list[root], heappop(cost_list[nxt]))
        rest_node = len(cost_list[root])
    print(res)


if __name__ == '__main__':
    resolve()
