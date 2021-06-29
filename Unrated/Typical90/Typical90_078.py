# https://atcoder.jp/contests/typical90/submissions/23861723
# 078 - Easy Graph Problem（★2）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n, m = map(int, input().split())
    edge = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        edge[a - 1].append(b - 1)
        edge[b - 1].append(a - 1)

    res = 0
    for v in range(n):
        cnt = 0
        for u in edge[v]:
            if v > u:
                cnt += 1
        if cnt == 1:
            res += 1
    print(res)


if __name__ == '__main__':
    solve()
