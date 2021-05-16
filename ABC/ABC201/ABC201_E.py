# https://atcoder.jp/contests/abc201/submissions/22649158
# E - Xor Distances
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    edge = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        edge[u - 1].append((w, v - 1))
        edge[v - 1].append((w, u - 1))

    dist = [-1] * n
    dist[0] = 0
    que = deque([0])
    while que:
        v = que.popleft()
        for w, u in edge[v]:
            if dist[u] != -1:
                continue
            dist[u] = dist[v] ^ w
            que.append(u)

    res = 0
    pow2 = 1
    for mask in range(60):
        cnt1 = sum(1 for d in dist if d & (1 << mask))
        t = cnt1 * (n - cnt1) % MOD
        res += pow2 * t % MOD
        res %= MOD
        pow2 *= 2
        pow2 %= MOD
    print(res)


if __name__ == '__main__':
    solve()
