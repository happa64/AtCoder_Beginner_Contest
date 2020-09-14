# https://atcoder.jp/contests/arc028/submissions/16748578
# C - 高橋王国の分割統治
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def dfs(v, p):
        for u in edge[v]:
            if u == p:
                continue
            cnt_list[v].append(dfs(u, v))

        res[v] = max(max(cnt_list[v]), n - sum(cnt_list[v]) - 1)
        return sum(cnt_list[v]) + 1

    n = int(input())
    edge = [[] for _ in range(n)]
    root = [True] * n
    for i in range(1, n):
        p = int(input())
        root[p] = False
        edge[i].append(p)
        edge[p].append(i)

    res = [0] * n
    cnt_list = [[0] for _ in range(n)]
    for i in range(n):
        if root[i]:
            s = i
            break
    dfs(s, -1)
    print(*res, sep="\n")


if __name__ == '__main__':
    resolve()
