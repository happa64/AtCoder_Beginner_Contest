# https://atcoder.jp/contests/abc181/submissions/17808044
# E - Transformable Teacher
import sys
from itertools import accumulate
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    H = [-f_inf] + list(map(int, input().split())) + [f_inf]
    W = list(map(int, input().split()))
    H.sort()
    W.sort()

    diff1 = []
    for i in range(1, n, 2):
        diff1.append(H[i + 1] - H[i])

    diff2 = []
    for i in range(2, n, 2):
        diff2.append(H[i + 1] - H[i])

    d1 = [0] + list(accumulate(diff1))
    d2 = [0] + list(accumulate(diff2))

    res = f_inf
    for w in W:
        tmp = 0
        idx = bisect_left(H, w)
        if idx % 2:
            tmp += d1[idx // 2]
            tmp += H[idx] - w
            tmp += d2[-1] - d2[idx // 2]
        else:
            tmp += d1[idx // 2 - 1]
            tmp += w - H[idx - 1]
            tmp += d2[-1] - d2[idx // 2 - 1]
        res = min(res, tmp)
    print(res)


if __name__ == '__main__':
    resolve()
