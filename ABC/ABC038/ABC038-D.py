# https://atcoder.jp/contests/abc038/submissions/14856708
# D - プレゼント
import sys
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    WH = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: [x[0], -x[1]])

    LIS = [WH[0][1]]
    for i in range(n):
        if WH[i][1] > LIS[-1]:
            LIS.append(WH[i][1])
        else:
            idx = bisect_left(LIS, WH[i][1])
            LIS[idx] = WH[i][1]
    print(len(LIS))


if __name__ == '__main__':
    resolve()
