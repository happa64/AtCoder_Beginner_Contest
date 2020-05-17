# https://atcoder.jp/contests/arc042/submissions/13145680
# A - 掲示板
import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    A = list(int(input()) for _ in range(m))

    double = defaultdict(int)
    res = []
    for i in reversed(range(m)):
        if double[A[i]] == 0:
            res.append(A[i])
            double[A[i]] = 1

    for j in range(1, n + 1):
        if double[j] == 0:
            res.append(j)

    for k in res:
        print(k)


if __name__ == '__main__':
    resolve()
