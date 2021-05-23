# https://atcoder.jp/contests/abc202/submissions/22839804
# E - Count Descendants
import sys
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7
idx = 0


def dfs(v, edge, depth, depth_list, in_list, out_list):
    global idx
    in_list[v] = idx
    idx += 1
    depth_list[depth[v]].append(in_list[v])
    for u in edge[v]:
        depth[u] = depth[v] + 1
        dfs(u, edge, depth, depth_list, in_list, out_list)
    out_list[v] = idx
    idx += 1


def solve():
    n = int(input())
    P = tuple(map(int, input().split()))
    q = int(input())

    edge = [[] for _ in range(n)]
    for i, p in enumerate(P, 1):
        edge[p - 1].append(i)

    depth = [0] * n
    depth_list = [[] for _ in range(n)]
    in_list = [0] * n
    out_list = [0] * n
    dfs(0, edge, depth, depth_list, in_list, out_list)

    for _ in range(q):
        u, d = map(int, input().split())
        u -= 1
        v = depth_list[d]
        l = bisect_left(v, out_list[u])
        r = bisect_left(v, in_list[u])
        res = l - r
        print(res)


if __name__ == '__main__':
    solve()
