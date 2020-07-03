import sys
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

    n, m = map(int, input().split())
    s, t = map(int, input().split())
    edge = [[] for _ in range(n)]
    for _ in range(m):
        x, y, d = map(int, input().split())
        edge[x - 1].append([d, y - 1])
        edge[y - 1].append([d, x - 1])

    d1 = dijkstra_heap(s - 1)
    d2 = dijkstra_heap(t - 1)
    for i in range(n):
        if d1[i] == 0 or d2[i] == 0:
            continue
        if d1[i] == d2[i] and d1[i] != f_inf:
            print(i + 1)
            break
    else:
        print(-1)


if __name__ == '__main__':
    resolve()
