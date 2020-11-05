# https://atcoder.jp/contests/abc061/submissions/17885593
# D - Score Attack
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    edge = [[] for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        edge[a - 1].append([-c, b - 1])

    update = [False] * n
    dist = [f_inf] * n
    dist[0] = 0
    for i in range(n):
        update = [False] * n
        for v in range(n):
            for d, u in edge[v]:
                if dist[v] != f_inf and dist[v] + d < dist[u]:
                    dist[u] = dist[v] + d
                    update[u] = True
    if update[-1]:
        print("inf")
    else:
        print(dist[-1] * -1)


if __name__ == '__main__':
    resolve()
