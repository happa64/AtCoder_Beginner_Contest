# https://atcoder.jp/contests/agc039/submissions/15364920
# B - Graph Partition
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def dfs(v, graph, cur=0):
        color[v] = cur
        for u in graph[v]:
            if color[u] != -1:
                if color[u] == cur:
                    return False
                continue
            if not dfs(u, graph, 1 - cur):
                return False
        return True

    n = int(input())
    S = [list(input()) for _ in range(n)]
    edge = [[] for _ in range(n)]
    cost = [[f_inf] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                cost[i][j] = 0
            if S[i][j] == "1":
                edge[i].append(j)
                cost[i][j] = 1

    color = [-1] * n
    if not dfs(0, edge):
        print(-1)
        exit()

    for k in range(n):
        for i in range(n):
            for j in range(n):
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

    res = 0
    for i in range(n):
        res = max(res, max(cost[i]))
    print(res + 1)


if __name__ == '__main__':
    resolve()
