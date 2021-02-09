# https://atcoder.jp/contests/tdpc/submissions/20074049
# K - ターゲット
import sys
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    LR = [[] for _ in range(n)]
    for i in range(n):
        x, r = map(int, input().split())
        LR[i] = [x - r, x + r]
    LR.sort()

    L = [r for _, r in LR][::-1]
    LIS = [L[0]]
    for i in range(len(L)):
        if L[i] > LIS[-1]:
            LIS.append(L[i])
        else:
            idx = bisect_left(LIS, L[i])
            LIS[idx] = L[i]
    print(len(LIS))


if __name__ == '__main__':
    resolve()
