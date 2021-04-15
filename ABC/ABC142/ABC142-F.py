import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    edge = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        edge[a - 1].append(b - 1)

    res = []
    shortest = n + 1
    for s in range(n):
        dist = [-1] * n
        prev = [-1] * n
        dist[s] = 0
        que = deque([s])
        while que:
            v = que.popleft()
            for nv in edge[v]:
                if dist[nv] == -1:
                    dist[nv] = dist[v] + 1
                    prev[nv] = v
                    que.append(nv)
        for t in range(n):
            if t == s or dist[t] == -1:
                continue
            for nt in edge[t]:
                if nt == s:
                    tmp = [s]
                    cur = t
                    while cur != s:
                        tmp.append(cur)
                        cur = prev[cur]
                    if shortest > len(tmp):
                        shortest = len(tmp)
                        res = tmp
    if shortest == n + 1:
        print(-1)
    else:
        print(len(res))
        print(*map(lambda x: int(x) + 1, res), sep="\n")


if __name__ == '__main__':
    resolve()
