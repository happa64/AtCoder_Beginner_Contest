# https://atcoder.jp/contests/past202012-open/submissions/19042672
# I - 避難計画
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def bfs(v):
        dist = [f_inf] * (n + 1)
        dist[v] = 0
        q = deque([v])
        while q:
            u = q.popleft()
            for v in edge[u]:
                if dist[v] == f_inf:
                    dist[v] = dist[u] + 1
                    q.append(v)
        return dist

    n, m, k = map(int, input().split())
    H = list(map(int, input().split()))
    C = list(map(lambda x: int(x) - 1, input().split()))
    edge = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        if H[a] > H[b]:
            edge[b].append(a)
        else:
            edge[a].append(b)
    for c in C:
        edge[n].append(c)

    res = bfs(n)
    for i in range(n):
        print(res[i] - 1 if res[i] != f_inf else -1)


if __name__ == '__main__':
    resolve()
