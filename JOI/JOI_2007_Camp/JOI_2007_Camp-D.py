# https://atcoder.jp/contests/joisc2007/submissions/16256982
# building - ビルの飾り付け (Building)
import sys
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    H = list(int(input()) for _ in range(n))

    LIS = [H[0]]
    for i in range(1, n):
        if LIS[-1] < H[i]:
            LIS.append(H[i])
        else:
            idx = bisect_left(LIS, H[i])
            LIS[idx] = H[i]
    print(len(LIS))


if __name__ == '__main__':
    resolve()
