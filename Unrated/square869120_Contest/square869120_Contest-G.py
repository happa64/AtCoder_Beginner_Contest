# https://atcoder.jp/contests/s8pc-1/submissions/15201164
# G - Revenge of Traveling Salesman Problem
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    graph = [[f_inf] * n for _ in range(n)]
    for _ in range(m):
        a, b, d, t = map(int, input().split())
        graph[a - 1][b - 1] = (d, t)
        graph[b - 1][a - 1] = (d, t)

    dist = [[f_inf] * n for _ in range(1 << n)]
    dist[0][0] = 0
    cnt = [[0] * n for _ in range(1 << n)]
    cnt[0][0] = 1
    for S in range(1 << n):
        for v in range(n):
            for u in range(n):
                if (S & (1 << v)) != 0 or graph[u][v] == f_inf:
                    continue
                d, t = graph[u][v]
                if t < dist[S][u] + d:
                    continue
                if dist[S][u] + d == dist[S | (1 << v)][v]:
                    cnt[S | (1 << v)][v] += cnt[S][u]
                elif dist[S][u] + d < dist[S | (1 << v)][v]:
                    dist[S | (1 << v)][v] = dist[S][u] + d
                    cnt[S | (1 << v)][v] = cnt[S][u]

    print("IMPOSSIBLE") if cnt[-1][0] == 0 else print(dist[-1][0], cnt[-1][0])


if __name__ == '__main__':
    resolve()
