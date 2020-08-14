# https://atcoder.jp/contests/nikkei2019-qual/submissions/15883291
# D - Restore the Tree
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    edge = [[] for _ in range(n)]
    edge_r = [[] for _ in range(n)]
    for _ in range(n - 1 + m):
        a, b = map(int, input().split())
        edge[a - 1].append(b - 1)
        edge_r[b - 1].append(a - 1)

    visited = [False] * n
    visited[0] = True
    que = deque([0])
    while que:
        v = que.popleft()
        if len(edge_r[v]) == 0:
            root = v
            break
        for u in edge_r[v]:
            if not visited[u]:
                visited[u] = True
                que.appendleft(u)

    cnt = [len(edge_r[i]) for i in range(n)]
    res = [[] for _ in range(n)]
    res[root].append(0)
    que = deque([root])
    while que:
        v = que.popleft()
        for u in edge[v]:
            if cnt[u] > 1:
                cnt[u] -= 1
            else:
                cnt[u] = 0
                que.appendleft(u)
                res[u].append(v + 1)

    for i in res:
        print(*i)


if __name__ == '__main__':
    resolve()
