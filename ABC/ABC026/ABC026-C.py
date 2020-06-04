# https://atcoder.jp/contests/abc026/submissions/13477800
# C - 高橋君の給料
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    tree = [[] for _ in range(n)]
    for i in range(1, n):
        b = int(input())
        tree[i].append(b - 1)
        tree[b - 1].append(i)

    def dfs(v, p):
        for u in tree[v]:
            if u == p:
                continue
            else:
                dfs(u, v)
                res = []
                for i in tree[u]:
                    if i == v:
                        continue
                    res.append(salary[i])
                if len(res) != 0:
                    salary[u] += min(res) + max(res)

    salary = [1 for _ in range(n)]
    dfs(0, - 1)

    t = []
    for i in tree[0]:
        t.append(salary[i])

    ans = 1 + min(t) + max(t)
    print(ans)


if __name__ == '__main__':
    resolve()
