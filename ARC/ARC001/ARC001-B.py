# https://atcoder.jp/contests/arc001/submissions/14445725
# B - リモコン
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b = map(int, input().split())
    edge = [[] for _ in range(61)]
    for i in range(51):
        edge[i].append(i + 1)
        edge[i + 1].append(i)

        edge[i].append(i + 5)
        edge[i + 5].append(i)

        edge[i].append(i + 10)
        edge[i + 10].append(i)

    def bfs(n):
        dist = [f_inf] * 61
        dist[n] = 0
        que = deque([n])
        while que:
            v = que.popleft()
            for u in edge[v]:
                if dist[u] == f_inf:
                    dist[u] = dist[v] + 1
                    que.append(u)
        return dist

    dist = bfs(a)
    print(dist[b])


if __name__ == '__main__':
    resolve()
