# https://atcoder.jp/contests/agc009/submissions/17126577
# B - Tournament
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def dfs(v):
        if len(edge[v]) == 0:
            return 0
        dp = []
        for u in edge[v]:
            dp.append(dfs(u))
        dp.sort(reverse=True)
        for i in range(len(dp)):
            dp[i] += i + 1
        return max(dp)

    n = int(input())
    edge = [[] for _ in range(n)]
    for i in range(1, n):
        a = int(input()) - 1
        edge[a].append(i)

    print(dfs(0))


if __name__ == '__main__':
    resolve()
