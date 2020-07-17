# https://atcoder.jp/contests/arc030/submissions/15284869
# B - ツリーグラフ
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def dfs(v, p):
        if H[v]:
            if len(edge) >= 1:
                for s, t in edge:
                    used.add((s, t))
        for u in tree[v]:
            if u == p:
                continue
            else:
                edge.append((v, u))
                dfs(u, v)
                edge.pop()

    n, x = map(int, input().split())
    H = list(map(int, input().split()))
    tree = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(lambda x: int(x) - 1, input().split())
        tree[a].append(b)
        tree[b].append(a)

    used = set()
    edge = []
    dfs(x - 1, -1)
    res = len(used) * 2
    print(res)


if __name__ == '__main__':
    resolve()
