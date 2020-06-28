# https://atcoder.jp/contests/abc172/submissions/14780789
# C - Tsundoku
import sys
from itertools import accumulate
from bisect import bisect_right

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A_ = [0] + list(accumulate(A))
    B_ = [0] + list(accumulate(B))

    init = bisect_right(A_, k)
    res = init - 1
    for i in range(init):
        t = k - A_[init - i - 1]
        idx = bisect_right(B_, t)
        res = max(res, init - i - 1 + idx - 1)

    print(res)


if __name__ == '__main__':
    resolve()
