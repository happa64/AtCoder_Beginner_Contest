# https://atcoder.jp/contests/abc126/submissions/13480923
# E - 1 or 2
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    """
    解法概要：
        カードは1と2しかなく、Ax+Ay+Zは偶数と決まっている為、Axiを決めた場合、Ayiは一意に定まる。
        また、Ax,Ayは根付き木としてみなす事ができ、AxiとAyiが連結であれば。あるAxi一点を決めれば他の値も位置に定まる。
        つまり、解は連結成分の数、という事になる。

    計算量：O(N)
    """
    n, m = map(int, input().split())

    tree = [[] for _ in range(n)]
    for _ in range(m):
        x, y, _ = map(int, input().split())
        tree[x - 1].append(y - 1)
        tree[y - 1].append(x - 1)

    def dfs(v):
        for u in tree[v]:
            if visited[u]:
                continue
            else:
                visited[u] = True
                dfs(u)

    visited = [False for _ in range(n)]
    res = 0
    for i in range(n):
        if not visited[i]:
            res += 1
            visited[i] = True
            dfs(i)

    print(res)


if __name__ == '__main__':
    resolve()
