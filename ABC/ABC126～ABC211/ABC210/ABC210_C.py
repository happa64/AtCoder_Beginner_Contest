# https://atcoder.jp/contests/abc210/submissions/24289552
# C - Colorful Candies
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n, k = map(int, input().split())
    C = list(map(int, input().split()))

    col = defaultdict(int)
    for i in range(k):
        col[C[i]] += 1

    res = len(col)
    for i in range(k, n):
        pre = C[i - k]
        col[pre] -= 1
        if col[pre] == 0:
            col.pop(pre)
        col[C[i]] += 1
        res = max(res, len(col))
    print(res)


if __name__ == '__main__':
    solve()
