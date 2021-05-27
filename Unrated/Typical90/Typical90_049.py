# https://atcoder.jp/contests/typical90/submissions/22948619
# 049 - Flip Digits 2（★6）
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


def solve():
    n, m = map(int, input().split())
    edge = []
    for _ in range(m):
        c, l, r = map(int, input().split())
        edge.append((c, l - 1, r))

    uf = UnionFind(n + 1)
    res = uf.kruskal(edge)
    root = uf.find(0)
    for i in range(1, n):
        if uf.find(i) != root:
            print(-1)
            break
    else:
        print(res)


if __name__ == '__main__':
    solve()
