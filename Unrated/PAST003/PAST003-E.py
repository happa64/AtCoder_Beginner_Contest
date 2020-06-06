# https://atcoder.jp/contests/past202005/submissions/13508695
# E - スプリンクラー
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m, q = map(int, input().split())
    tree = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        tree[u - 1].append(v - 1)
        tree[v - 1].append(u - 1)
    color = list(map(int, input().split()))
    query = [list(map(int, input().split())) for _ in range(q)]

    for i in range(q):
        if query[i][0] == 1:
            _, x = query[i]
            print(color[x - 1])
            for u in tree[x - 1]:
                color[u] = color[x - 1]
        else:
            _, x, y = query[i]
            print(color[x - 1])
            color[x - 1] = y


if __name__ == '__main__':
    resolve()
