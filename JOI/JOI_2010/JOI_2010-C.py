# https://atcoder.jp/contests/joi2010ho/submissions/18988456
# C - つらら
import sys
from heapq import *

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, l = map(int, input().split())
    A = list(int(input()) for _ in range(n))

    que = [[l - a, i + 1] for i, a in enumerate(A)]
    heapify(que)

    res = [0] * (n + 2)
    wait = [0] * (n + 2)
    while que:
        diff, idx = heappop(que)
        res[idx] = max(wait[idx - 1], wait[idx + 1]) + diff
        wait[idx] += res[idx]

    print(max(res))


if __name__ == '__main__':
    resolve()
