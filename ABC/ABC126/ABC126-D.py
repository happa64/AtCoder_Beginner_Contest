# https://atcoder.jp/contests/abc126/submissions/14888783
# D - Even Relation
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def dfs(v, p):
        for u, w in tree[v]:
            if u == p:
                continue
            else:
                dist[u] = dist[v] + w
                dfs(u, v)

    n = int(input())
    tree = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        tree[u - 1].append([v - 1, w])
        tree[v - 1].append([u - 1, w])

    dist = [0] * n
    dfs(0, -1)
    res = []
    for d in dist:
        res.append(0 if d % 2 == 0 else 1)
    print(*res, sep="\n")


if __name__ == '__main__':
    resolve()
