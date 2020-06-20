# https://atcoder.jp/contests/abc130/submissions/14485233
# D - Enough Array
import sys
from itertools import accumulate
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    """
    尺取り法
    """
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    res = 0
    left = 0
    total = 0
    for right in range(n):
        total += A[right]
        while total >= k:
            res += n - right
            total -= A[left]
            left += 1

    print(res)


def resolve2():
    """
    累積和＋二分探索
    """
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    B = [0] + list(accumulate(A))
    res = 0
    for i in range(1, n + 1):
        res += n - bisect_left(B, B[i - 1] + k) + 1
    print(res)


if __name__ == '__main__':
    resolve()
