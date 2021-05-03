# https://atcoder.jp/contests/typical90/submissions/21932073
# 012 - Red Painting（★4）
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
    H, W = map(int, input().split())
    grid = [["W"] * W for _ in range(H)]
    uf = UnionFind(H * W)
    q = int(input())
    for _ in range(q):
        t, *query = map(lambda x: int(x) - 1, input().split())
        if t == 0:
            r, c = query
            grid[r][c] = "R"
            v = r * W + c
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= H or nc >= W:
                    continue
                if grid[nr][nc] == "R":
                    u = nr * W + nc
                    uf.union(v, u)
        else:
            ra, ca, rb, cb = query
            v = ra * W + ca
            u = rb * W + cb
            print("Yes" if grid[ra][ca] == grid[rb][cb] == "R" and uf.same(v, u) else "No")


if __name__ == '__main__':
    solve()
