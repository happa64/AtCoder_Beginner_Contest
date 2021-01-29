# https://atcoder.jp/contests/agc008/submissions/19747259
# B - Contiguous Repainting
import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    A_sum = [0] + list(accumulate(A))
    A_plus_sum = [0]
    for a in A:
        A_plus_sum.append(A_plus_sum[-1] + (a if a >= 0 else 0))

    res = 0
    for i in range(n - k + 1):
        white = A_plus_sum[-1] - (A_plus_sum[i + k] - A_plus_sum[i])
        black = white + (A_sum[i + k] - A_sum[i])
        res = max(res, white, black)
    print(res)


if __name__ == '__main__':
    resolve()
