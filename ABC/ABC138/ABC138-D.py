# https://atcoder.jp/contests/abc138/submissions/13630907
# D - Ki
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, q = map(int, input().split())

    tree = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        tree[a - 1].append(b - 1)
        tree[b - 1].append(a - 1)

    cnt = [0] * n
    for _ in range(q):
        p, x = map(int, input().split())
        cnt[p - 1] += x

    def dfs(v, p):
        for u in tree[v]:
            if u == p:
                continue
            cnt[u] += cnt[v]
            dfs(u, v)

    dfs(0, -1)
    print(*cnt)


if __name__ == '__main__':
    resolve()
