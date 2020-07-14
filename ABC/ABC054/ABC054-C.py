# https://atcoder.jp/contests/abc054/submissions/15232421
# C - One-stroke Path
import sys
from itertools import permutations

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    """
    順列を全部試す。計算量O(N!)
    """
    n, m = map(int, input().split())
    tree = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        tree[a - 1].append(b - 1)
        tree[b - 1].append(a - 1)

    res = 0
    for pattern in permutations(range(n)):
        if pattern[0] == 0:
            for i in range(n - 1):
                if pattern[i + 1] not in tree[pattern[i]]:
                    break
            else:
                res += 1
    print(res)


def resolve2():
    """
    bit DP。計算量O(2^N*N^2)
    """
    n, m = map(int, input().split())
    edge = [[f_inf] * n for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        edge[a - 1][b - 1] = 1
        edge[b - 1][a - 1] = 1

    dp = [[f_inf] * n for _ in range(1 << n)]
    dp[0][0] = 0
    cnt = [[0] * n for _ in range(1 << n)]
    cnt[0][0] = 1
    for S in range(1 << n):
        for v in range(n):
            for u in range(n):
                if v == u or S & (1 << v) or edge[u][v] == f_inf:
                    continue
                if dp[S | (1 << v)][v] > dp[S][u] + edge[u][v]:
                    dp[S | (1 << v)][v] = dp[S][u] + edge[u][v]
                    cnt[S | (1 << v)][v] = cnt[S][u]
                elif dp[S | (1 << v)][v] == dp[S][u] + edge[u][v]:
                    cnt[S | (1 << v)][v] += cnt[S][u]

    mi = min(dp[-2])
    idx = []
    for i in range(n):
        if dp[-2][i] == mi:
            idx.append(i)

    res = 0
    for j in idx:
        res += cnt[-2][j]
    print(res)


if __name__ == '__main__':
    resolve2()
