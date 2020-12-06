# https://atcoder.jp/contests/abc102/submissions/18611943
# D - Equal Cut
import sys
from itertools import accumulate
from bisect import bisect_right

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    Acc = [0] + list(accumulate(A))
    res = f_inf
    for i in range(2, n - 1):
        left = Acc[i]
        right = Acc[-1] - Acc[i]
        left_half = left // 2
        right_half = left + right // 2
        idx_left = bisect_right(Acc, left_half)
        idx_right = bisect_right(Acc, right_half)
        for j in [idx_left - 1, idx_left, idx_left + 1]:
            if j <= 0:
                continue
            left_l = Acc[j]
            left_r = left - left_l
            for k in [idx_right - 1, idx_right, idx_right + 1]:
                if k >= n:
                    continue
                right_l = Acc[k] - Acc[i]
                right_r = Acc[-1] - Acc[k]
                ma = max(left_l, left_r, right_l, right_r)
                mi = min(left_l, left_r, right_l, right_r)
                res = min(res, abs(ma - mi))
    print(res)


if __name__ == '__main__':
    resolve()
