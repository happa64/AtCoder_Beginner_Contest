import sys
from collections import deque
import heapq

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def dijkstra_heap(s):
        d = [f_inf] * n
        used = [True] * n
        d[s] = 0
        used[s] = False
        edgelist = []
        for e in edge[s]:
            heapq.heappush(edgelist, e)
        while len(edgelist):
            minedge = heapq.heappop(edgelist)
            if not used[minedge[1]]:
                continue
            v = minedge[1]
            d[v] = minedge[0]
            used[v] = False
            for e in edge[v]:
                if used[e[1]]:
                    heapq.heappush(edgelist, [e[0] + d[v], e[1]])
        return d

    n, m, k, s = map(int, input().split())
    P, Q = map(int, input().split())
    C = list(int(input()) - 1 for _ in range(k))
    C_s = set(C)
    tree = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        tree[a - 1].append(b - 1)
        tree[b - 1].append(a - 1)

    danger = set()
    for c in C:
        dist = [f_inf] * n
        dist[c] = 0
        que = deque([c])
        while que:
            v = que.popleft()
            if dist[v] == s:
                continue
            for u in tree[v]:
                if dist[u] == f_inf:
                    dist[u] = dist[v] + 1
                    que.append(u)
                    danger.add(u)

    edge = [[] for _ in range(n)]
    check = set()
    que2 = deque([0])
    while que2:
        v = que2.popleft()
        cost_v = 0 if v == 0 or v == n - 1 else f_inf if v in C_s else Q if v in danger else P
        for u in tree[v]:
            if (u, v) not in check or (v, u) not in check:
                cost_u = 0 if u == 0 or u == n - 1 else f_inf if u in C_s else Q if u in danger else P
                edge[v].append([cost_u, u])
                edge[u].append([cost_v, v])
                check.add((u, v))
                check.add((v, u))
                que2.append(u)

    res = dijkstra_heap(0)
    print(res[-1])


if __name__ == '__main__':
    resolve()
