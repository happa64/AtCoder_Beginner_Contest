# https://atcoder.jp/contests/past201912-open/submissions/13682003
# K - 巨大企業
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7
idx = 0


def resolve():
    n = int(input())

    root = 0
    tree = [[] for _ in range(n)]
    for i in range(n):
        p = int(input())
        if p == -1:
            root = i
            continue
        tree[p - 1].append(i)
        tree[i].append(p - 1)

    # オイラーツアー
    def dfs(v, p):
        global idx
        begin[v] = idx
        idx += 1
        for u in tree[v]:
            if u == p:
                continue
            dfs(u, v)
        end[v] = idx
        idx += 1

    begin = [0] * n
    end = [0] * n
    dfs(root, -1)
    q = int(input())
    for _ in range(q):
        a, b = map(int, input().split())
        print("Yes" if begin[b - 1] < begin[a - 1] and end[a - 1] < end[b - 1] else "No")


if __name__ == '__main__':
    resolve()
