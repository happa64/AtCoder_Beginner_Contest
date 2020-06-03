# https://atcoder.jp/contests/abc016/submissions/13113300
# C - 友達の友達
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())

    tree = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        tree[a - 1].append(b - 1)
        tree[b - 1].append(a - 1)

    # 幅優先探索でvから各頂点への距離を計算
    def bfs(v):
        dist = [f_inf for _ in range(n)]
        dist[v] = 0
        q = deque()
        q.append(v)
        while q:
            u = q.popleft()
            for nv in tree[u]:
                if dist[nv] == f_inf:
                    dist[nv] = dist[u] + 1
                    q.append(nv)

        # vからの距離が2であれば友達の友達
        res = 0
        for i in dist:
            if i == 2:
                res += 1

        return res

    for i in range(n):
        print(bfs(i))


if __name__ == '__main__':
    resolve()
