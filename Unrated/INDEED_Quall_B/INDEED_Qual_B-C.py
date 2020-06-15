# https://atcoder.jp/contests/indeednow-qualb/submissions/14386689
# C - 木
import sys
from heapq import heapify, heappop, heappush

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def bfs(i):
        num = []
        que = [i]
        heapify(que)
        while que:
            v = heappop(que)
            visited[v] = True
            num.append(v + 1)
            for u in tree[v]:
                if not visited[u]:
                    heappush(que, u)
        return num

    n = int(input())
    tree = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        tree[a - 1].append(b - 1)
        tree[b - 1].append(a - 1)

    visited = [False] * n
    res = bfs(0)
    print(*res)


if __name__ == '__main__':
    resolve()
