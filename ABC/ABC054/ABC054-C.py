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
    edge = set(tuple(tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)))

    dp = [[0] * n for _ in range(1 << n)]
    dp[1][0] = 1
    for S in range(1 << n):
        if not (S & 1):
            continue
        if S == 1:
            for v in range(n):
                if S & (1 << v):
                    continue
                if (0, v) in edge or (v, 0) in edge:
                    dp[S | (1 << v)][v] += dp[S][0]
        else:
            for u in range(1, n):
                if not (S & (1 << u)):
                    continue
                for v in range(n):
                    if S & (1 << v):
                        continue
                    if (u, v) in edge or (v, u) in edge:
                        dp[S | (1 << v)][v] += dp[S][u]
    print(sum(dp[-1]))


if __name__ == '__main__':
    resolve2()
