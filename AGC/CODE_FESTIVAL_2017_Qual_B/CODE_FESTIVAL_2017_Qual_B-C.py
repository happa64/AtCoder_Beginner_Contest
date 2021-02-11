# https://atcoder.jp/contests/code-festival-2017-qualb/submissions/20097244
# C - 3 Steps
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def dfs(v, c):
        col[v] = c
        for u in edge[v]:
            if col[u] == c:
                return False
            if col[u] is None and not dfs(u, c ^ 1):
                return False
        return True

    n, m = map(int, input().split())
    edge = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        edge[a].append(b)
        edge[b].append(a)

    col = [None] * n
    flg = dfs(0, 0)

    if flg:
        cnt_0 = sum(col[i] == 0 for i in range(n))
        cnt_1 = sum(col[i] == 1 for i in range(n))
        res = 0
        for i in range(n):
            tmp = cnt_1 if col[i] == 0 else cnt_0
            for u in edge[i]:
                if col[u] != col[i]:
                    tmp -= 1
            res += tmp
        print(res // 2)
    else:
        res = (n - 1) * n // 2 - m
        print(res)


if __name__ == '__main__':
    resolve()
