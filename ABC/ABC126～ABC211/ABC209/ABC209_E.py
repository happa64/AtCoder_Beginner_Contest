# https://atcoder.jp/contests/abc209/submissions/24718852
# E - Shiritori
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    S = tuple(input().rstrip() for _ in range(n))

    i = 0
    ind = defaultdict(int)
    for s in S:
        a = s[:3]
        b = s[-3:]
        if ind.get(a) is None:
            ind[a] = i
            i += 1
        if ind.get(b) is None:
            ind[b] = i
            i += 1

    m = len(ind)
    cnt = [0] * m
    edge = [[] for _ in range(m)]
    r_edge = [[] for _ in range(m)]
    for s in S:
        u = ind[s[:3]]
        v = ind[s[-3:]]
        edge[u].append(v)
        cnt[u] += 1
        r_edge[v].append(u)

    win = [-1] * m
    que = deque()
    for i in range(m):
        if not cnt[i]:
            win[i] = 0
            que.append(i)

    while que:
        v = que.popleft()
        for u in r_edge[v]:
            if win[u] != -1:
                continue
            cnt[u] -= 1
            if not win[v]:
                win[u] = 1
                que.append(u)
            elif not cnt[u]:
                win[u] = 0
                que.append(u)

    for s in S:
        idx = ind[s[-3:]]
        print("Takahashi" if not win[idx] else "Aoki" if win[idx] == 1 else "Draw")


if __name__ == '__main__':
    solve()
