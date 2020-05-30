# https://atcoder.jp/contests/past201912-open/submissions/13710103
# L - グラデーション
import sys
from itertools import product
import copy

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


# Union Find（経路圧縮有）
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    # 親が同じか判別
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    # 根を繋ぎ直す
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    # 親が同じか判別
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # 連結成分の大きさを返す
    def size(self, x):
        return -self.parents[self.find(x)]


def calc_cost(x1, y1, c1, x2, y2, c2):
    op = 1 if c1 == c2 else 10
    return pow(pow(x1 - x2, 2) + pow(y1 - y2, 2), 0.5) * op


def resolve():
    n, m = map(int, input().split())
    large_tower = [list(map(int, input().split())) for _ in range(n)]
    small_tower = [list(map(int, input().split())) for _ in range(m)]

    # edge_init：大きい塔同士に建設する橋のコスト
    edge_init = []
    for i in range(n):
        x1, y1, c1 = large_tower[i]
        for j in range(i + 1, n):
            x2, y2, c2 = large_tower[j]
            edge_init.append((calc_cost(x1, y1, c1, x2, y2, c2), i, j))

    res = f_inf
    # 小さい塔を経由するパターンを全て試す
    for pattern in product([0, 1], repeat=m):
        edge = copy.deepcopy(edge_init)
        sub_set = [idx for idx, p in enumerate(pattern) if p]

        # 大きい塔と小さい塔に建設する橋のコスト
        for i in range(n):
            x1, y1, c1 = large_tower[i]
            for j in sub_set:
                x2, y2, c2 = small_tower[j]
                edge.append((calc_cost(x1, y1, c1, x2, y2, c2), i, n + j))

        # 小さい塔同士に建設する橋のコスト
        for i in sub_set:
            x1, y1, c1 = small_tower[i]
            for j in sub_set:
                if i != j:
                    x2, y2, c2 = small_tower[j]
                    edge.append((calc_cost(x1, y1, c1, x2, y2, c2), n + i, n + j))

        # クラスカル法
        edge.sort(key=lambda x: x[0])
        uf = UnionFind(n + m)
        cost_sum = 0
        for cost, a, b in edge:
            if not uf.same(a, b):
                cost_sum += cost
                uf.union(a, b)
        res = min(res, cost_sum)

    print(res)


if __name__ == '__main__':
    resolve()
