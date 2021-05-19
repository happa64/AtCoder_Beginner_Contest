# https://atcoder.jp/contests/typical90/submissions/22573242
# 039 - Tree Distance（★5）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    def dfs(v, p):
        for u in edge[v]:
            if u == p:
                continue
            dfs(u, v)
        if p != -1:
            dp[p] += dp[v]

    n = int(input())
    edge = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(lambda x: int(x) - 1, input().split())
        edge[a].append(b)
        edge[b].append(a)

    dp = [1] * n
    dfs(0, -1)
    res = 0
    for i in dp:
        res += (n - i) * i
    print(res)


if __name__ == '__main__':
    solve()
