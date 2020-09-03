# https://atcoder.jp/contests/abc030/submissions/16476887
# D - へんてこ辞書
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def dfs(v, d):
        dist[v] = d
        for u in edge[v]:
            if dist[u] != f_inf:
                cycle.append([dist[u], dist[v] + 1])
                return
            else:
                dfs(u, d + 1)

    n, a = map(int, input().split())
    k = int(input())
    B = list(map(int, input().split()))
    edge = [[] for _ in range(n)]
    for i in range(n):
        edge[i].append(B[i] - 1)

    cycle = []
    dist = [f_inf] * n
    dfs(a - 1, 0)

    cycle_start = cycle[0][0]
    cycle_end = cycle[0][1]
    if k <= cycle_start:
        print(dist.index(k) + 1)
    else:
        remainder = (k - cycle_start) % (cycle_end - cycle_start)
        res = cycle_start + remainder
        print(dist.index(res) + 1)


if __name__ == '__main__':
    resolve()
