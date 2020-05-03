# https://atcoder.jp/contests/abc010/tasks/abc010_4
# D - 浮気予防（９９点解法）
import sys
from itertools import product

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, g, e = map(int, input().split())
    P = list(map(int, input().split()))
    tree = [[] for _ in range(n)]
    edge = []
    for _ in range(e):
        a, b = map(int, input().split())
        edge.append([a, b])
        tree[a].append(b)
        tree[b].append(a)

    # 深さ優先探索
    def dfs(v):
        for u in tree[v]:
            if [v, u] in removed or [u, v] in removed:
                continue
            elif visited[u]:
                continue
            else:
                visited[u] = True
                dfs(u)

    res = f_inf
    # 解消する友人関係のパターンを全列挙2^E
    for pattern in product([0, 1], repeat=e):
        removed = []
        for i in range(e):
            if pattern[i] == 1:
                removed.append(edge[i])

        visited = [False for _ in range(n)]
        dfs(0)
        cnt = 0
        # 友人関係を解消したにも関わらず、髙橋君と友人関係にある場合は、ログイン不可にさせる
        for p in P:
            if visited[p]:
                cnt += 1
        res = min(res, sum(pattern) + cnt)

    print(res)


if __name__ == '__main__':
    resolve()
