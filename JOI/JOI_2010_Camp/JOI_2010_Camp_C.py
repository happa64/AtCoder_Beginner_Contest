# https://atcoder.jp/contests/joisc2010/submissions/18971334
# stairs - 階段 (Stairs)
import sys
from bisect import bisect_left
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 1234567


def resolve():
    n, p = map(int, input().split())
    H = tuple(int(input()) for _ in range(n))
    H_sum = [0] + list(accumulate(H))

    res = 0
    dp_sum = [0] * (n + 2)
    dp_sum[1] = 1
    for i in range(1, n + 1):
        idx = bisect_left(H_sum, H_sum[i] - p)
        res = (dp_sum[i] - dp_sum[idx]) % mod
        dp_sum[i + 1] = (dp_sum[i] + res) % mod
    print(res % mod)


if __name__ == '__main__':
    resolve()
