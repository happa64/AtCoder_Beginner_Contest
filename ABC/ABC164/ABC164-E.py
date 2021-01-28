# https://atcoder.jp/contests/abc164/submissions/19736542
# E - Two Currencies
import sys
from heapq import heappop, heappush

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m, s = map(int, input().split())
    MAX = (n - 1) * 50
    s = min(s, MAX)
    edge = [[[] for _ in range(MAX + 1)] for _ in range(n)]
    for _ in range(m):
        u, v, a, b = map(int, input().split())
        for i in range(MAX + 1):
            if i - a >= 0:
                edge[u - 1][i].append((b, v - 1, i - a))
                edge[v - 1][i].append((b, u - 1, i - a))
    for u in range(n):
        c, d = map(int, input().split())
        for j in range(c, MAX + 1):
            edge[u][j - c].append((d, u, j))

    dp = [[f_inf] * (MAX + 1) for _ in range(n)]
    dp[0][s] = 0
    edge_list = []
    for u in edge[0][s]:
        heappush(edge_list, u)
    while edge_list:
        cost, node, state = heappop(edge_list)
        if dp[node][state] == f_inf:
            dp[node][state] = cost
            for next_cost, next_node, next_state in edge[node][state]:
                if dp[next_node][next_state] == f_inf:
                    heappush(edge_list, (next_cost + cost, next_node, next_state))

    for i in range(1, n):
        print(min(dp[i][j] for j in range(MAX + 1)))


if __name__ == '__main__':
    resolve()
