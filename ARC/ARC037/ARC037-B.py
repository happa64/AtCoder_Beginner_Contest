# https://atcoder.jp/contests/arc037/submissions/14455642
# B - バウムテスト
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def dfs(v, p):
        for u in tree[v]:
            if u == p:
                continue
            elif visited[u]:
                cnt[u] += 1
            else:
                visited[u] = True
                cnt[u] += 1
                dfs(u, v)

    n, m = map(int, input().split())
    tree = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        tree[u - 1].append(v - 1)
        tree[v - 1].append(u - 1)

    visited = [False] * n
    res = 0
    for i in range(n):
        if not visited[i]:
            cnt = [0] * n
            visited[i] = True
            cnt[i] = 1
            dfs(i, -1)
            for j in cnt:
                if j > 1:
                    break
            else:
                res += 1
    print(res)


if __name__ == '__main__':
    resolve()
