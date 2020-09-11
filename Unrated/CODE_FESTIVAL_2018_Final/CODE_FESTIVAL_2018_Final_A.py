# https://atcoder.jp/contests/code-festival-2018-final-open/submissions/16628292
# A - 2540
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    edge = [defaultdict(int) for _ in range(n)]
    for _ in range(m):
        a, b, l = map(int, input().split())
        edge[a - 1][l] += 1
        edge[b - 1][l] += 1

    res = 0
    for i in range(n):
        for k, v in edge[i].items():
            if k == 1270:
                res += v * (v - 1) // 2
            else:
                if edge[i].get(2540 - k, -1) != -1:
                    res += edge[i][2540 - k] * v
            edge[i][k] = 0
    print(res)


if __name__ == '__main__':
    resolve()
