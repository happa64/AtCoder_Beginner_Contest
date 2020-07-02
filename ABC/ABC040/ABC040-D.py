# https://atcoder.jp/contests/abc040/submissions/14898220
#D - 道路の老朽化対策について
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
    n, m = map(int, input().split())
    edge = sorted([list(map(int, input().split())) for _ in range(m)], key=lambda x: -x[2])
    q = int(input())
    query = []
    for i in range(q):
        v, w = map(int, input().split())
        query.append([v - 1, w, i])
    query.sort(key=lambda x: -x[1])

    uf = UnionFind(n)
    res = [0] * q
    i = 0
    for v, w, idx in query:
        while i < m and edge[i][2] > w:
            a, b, _ = edge[i]
            uf.union(a - 1, b - 1)
            i += 1
        res[idx] = uf.size(v)
    print(*res, sep="\n")


if __name__ == '__main__':
    resolve()
