# https://atcoder.jp/contests/joi2009ho/submissions/14938004
# B - ピザ
import sys
from bisect import bisect_right

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    d = int(input())
    n = int(input())
    m = int(input())
    D = sorted([0] + list(int(input()) for _ in range(n - 1)) + [d])

    res = 0
    for _ in range(m):
        k = int(input())
        idx = bisect_right(D, k)
        res += min(abs(D[idx] - k), abs(D[idx - 1] - k))
    print(res)


if __name__ == '__main__':
    resolve()
