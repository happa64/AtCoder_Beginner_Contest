# https://atcoder.jp/contests/joi2010yo/submissions/16237751
# C - パーティー
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    m = int(input())
    edge = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        edge[a - 1].append(b - 1)
        edge[b - 1].append(a - 1)

    que = deque([0])
    dist = [f_inf] * n
    dist[0] = 0
    res = 0
    while que:
        v = que.popleft()
        for u in edge[v]:
            if dist[u] == f_inf:
                dist[u] = dist[v] + 1
                if dist[u] == 1 or dist[u] == 2:
                    res += 1
                que.append(u)
    print(res)


if __name__ == '__main__':
    resolve()
