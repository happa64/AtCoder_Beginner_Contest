# https://atcoder.jp/contests/abc157/submissions/14487133
# D - Friend Suggestions
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


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


def resolve():
    n, m, k = map(int, input().split())
    uf = UnionFind(n)
    edge = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        uf.union(a - 1, b - 1)
        edge[a - 1].append(b - 1)
        edge[b - 1].append(a - 1)

    block = [[] for _ in range(n)]
    for _ in range(k):
        c, d = map(int, input().split())
        if uf.same(c - 1, d - 1):
            block[c - 1].append(d - 1)
            block[d - 1].append(c - 1)

    res = []
    for i in range(n):
        res.append(uf.size(i) - (len(edge[i]) + 1) - (len(block[i])))
    print(*res)


if __name__ == '__main__':
    resolve()
