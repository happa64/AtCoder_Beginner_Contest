# https://atcoder.jp/contests/abc160/submissions/13597634
# D - Line++
import sys
from collections import deque
sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, x, y = map(int, input().split())
    tree = [[] for _ in range(n)]
    for i in range(1, n):
        tree[i - 1].append(i)
        tree[i].append(i - 1)

    tree[x - 1].append(y - 1)
    tree[y - 1].append(x - 1)

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

        for d in dist:
            res[d] += 1

    res = [0 for _ in range(n)]
    for i in range(n):
        bfs(i)

    for j in range(1, n):
        print(res[j] // 2)


if __name__ == '__main__':
    resolve()
