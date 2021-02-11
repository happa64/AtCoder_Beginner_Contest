# https://atcoder.jp/contests/maximum-cup-2018/submissions/20096776
# C - 嘘つきな天使たち
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def main():
    def dfs(v, c):
        col[v] = c
        for u in edge[v]:
            if col[u] is None:
                dfs(u, c ^ 1)
            else:
                if col[u] == col[v]:
                    print(-1)
                    exit()

    n = int(input())
    edge = [[] for _ in range(n)]
    for i in range(n):
        a = int(input()) - 1
        edge[a].append(i)
        edge[i].append(a)

    col = [None] * n
    for i in range(n):
        if col[i] is not None:
            continue
        dfs(i, 0)
    print(max(sum(col), n - sum(col)))


if __name__ == '__main__':
    main()
