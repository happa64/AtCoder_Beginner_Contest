# https://atcoder.jp/contests/abc017/submissions/16017022
# C - ハイスコア
import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    LRS = [list(map(int, input().split())) for _ in range(n)]

    total = 0
    imos = [0] * (m + 2)
    for l, r, s in LRS:
        total += s
        imos[l] += s
        imos[r + 1] -= s

    imos = list(accumulate(imos))
    res = total - min(imos[1: m + 1])
    print(res)


if __name__ == '__main__':
    resolve()
