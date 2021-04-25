# https://atcoder.jp/contests/past202104-open/submissions/22052270
# L - 都市計画
import sys
from copy import deepcopy

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


def calc_dist(x1, y1, x2, y2):
    return pow(x1 - x2, 2) + pow(y1 - y2, 2)


def calc_dist_circle(x1, y1, r1, x2, y2, r2):
    d = pow(calc_dist(x1, y1, x2, y2), 0.5)
    if r1 < r2:
        r1, r2 = r2, r1
    if d > r1 + r2:
        return d - r1 - r2
    elif d < r1 - r2:
        return r1 - r2 - d
    else:
        return 0


def solve():
    n, m = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(n)]
    C = [list(map(int, input().split())) for _ in range(m)]

    init = []
    for i in range(n):
        x1, y1 = T[i]
        for j in range(i + 1, n):
            x2, y2 = T[j]
            d = pow(calc_dist(x1, y1, x2, y2), 0.5)
            init.append([d, i, j])

    res = f_inf
    for bit in range(1 << m):
        edge = deepcopy(init)
        circle = [C[i] for i in range(m) if bit & (1 << i)]
        k = len(circle)
        for i in range(n):
            x1, y1 = T[i]
            for j in range(k):
                x2, y2, r = circle[j]
                d = abs(pow(calc_dist(x1, y1, x2, y2), 0.5) - r)
                edge.append([d, i, n + j])
        for i in range(k):
            x1, y1, r1 = circle[i]
            for j in range(i + 1, k):
                x2, y2, r2 = circle[j]
                d = calc_dist_circle(x1, y1, r1, x2, y2, r2)
                edge.append([d, n + i, n + j])
        uf = UnionFind(n + k)
        dist = uf.kruskal(edge)
        res = min(res, dist)
    print(res)


if __name__ == '__main__':
    solve()
