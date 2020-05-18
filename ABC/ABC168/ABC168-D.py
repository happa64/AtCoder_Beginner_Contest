# https://atcoder.jp/contests/abc168/submissions/13327879
# D - .. (Double Dots)
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

    # 全部の辺を辿って到達できない場所があればNoである
    def dfs(v, p):
        for u in tree[v]:
            if u == p:
                continue
            elif visited[u]:
                continue
            else:
                visited[u] = True
                dfs(u, v)

    visited = [False for _ in range(n)]
    visited[0] = True
    dfs(0, -1)
    for i in visited:
        if not i:
            print("No")
            exit()

    # 幅優先探索をして、各ノードに直上のノードの印をつけていく
    def bfs(v):
        pre = [-1 for _ in range(n)]
        pre[0] = 0
        q = deque()
        q.append(v)
        while q:
            u = q.popleft()
            for nv in tree[u]:
                if pre[nv] == -1:
                    pre[nv] = u
                    q.append(nv)
        return pre

    res = bfs(0)
    print("Yes")
    for i in range(1, n):
        print(res[i] + 1)


if __name__ == '__main__':
    resolve()
