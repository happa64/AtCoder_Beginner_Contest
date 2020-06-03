# https://atcoder.jp/contests/abc021/submissions/13941098
# C - 正直者の高橋くん
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    a, b = map(int, input().split())
    m = int(input())
    tree = [[] for _ in range(n)]
    for _ in range(m):
        x, y = map(int, input().split())
        tree[x - 1].append(y - 1)
        tree[y - 1].append(x - 1)

    def bfs(v):
        """
        :param v: 始点v
        :return: 始点vから各頂点への最短距離
        """
        dist = [f_inf for _ in range(n)]
        dist[v] = 0
        q = deque()
        q.append(v)
        while q:
            u = q.popleft()
            for nv in tree[u]:
                if dist[nv] == f_inf:
                    dist[nv] = dist[u] + 1
                    q.append(nv)

        return dist

    # aからbまでの最短経路に含まれない頂点を探す
    not_available = set()
    dist = bfs(a - 1)
    min_dist = dist[b - 1]
    for i in range(n):
        t = bfs(i)
        if t[a - 1] + t[b - 1] != min_dist:
            not_available.add(i)

    def bfs2(v):
        """
        経由する頂点から出ている辺の数の積をとる
        :param v: 始点a
        :return: a~bへの最短経路の個数(mod 10**9+7)
        """
        res = 1
        visited = [False for _ in range(n)]
        visited[v] = True
        q = deque()
        q.append(v)
        while q:
            u = q.popleft()
            cnt = 0
            for nv in tree[u]:
                if nv in not_available:
                    continue
                elif visited[nv]:
                    continue
                else:
                    visited[nv] = True
                    cnt += 1
                    q.append(nv)
            if cnt:
                res *= cnt
                res %= mod

        return res

    print(bfs2(a - 1) % mod)


if __name__ == '__main__':
    resolve()
