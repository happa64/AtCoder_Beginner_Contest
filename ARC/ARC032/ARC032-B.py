# https://atcoder.jp/contests/arc032/submissions/13473867
# B - 道路工事
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())

    # UnionFind木
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

    uf = UnionFind(n)

    # 入力されるaとbを連結させる
    for _ in range(m):
        a, b = map(int, input().split())
        uf.union(a - 1, b - 1)

    res = 0
    # 0（根）とそれ以外が連結でなければ連結させ、カウントアップする
    for i in range(1, n):
        if not uf.same(0, i):
            res += 1
            uf.union(0, i)

    print(res)


def resolve2():
    n, m = map(int, input().split())
    tree = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        tree[a - 1].append(b - 1)
        tree[b - 1].append(a - 1)

    def dfs(v):
        for u in tree[v]:
            if visited[u]:
                continue
            else:
                visited[u] = True
                dfs(u)

    visited = [False for _ in range(n)]
    res = -1
    for i in range(n):
        if not visited[i]:
            res += 1
            dfs(i)

    print(res)


if __name__ == '__main__':
    resolve2()
