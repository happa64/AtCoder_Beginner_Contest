# https://atcoder.jp/contests/typical90/submissions/21908951
# 007 - CP Classes（★3）
import sys
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    _ = int(input())
    A = [-f_inf] + list(map(int, input().split())) + [f_inf]
    A.sort()

    q = int(input())
    for _ in range(q):
        b = int(input())
        idx = bisect_left(A, b)
        l = abs(b - A[idx - 1])
        r = abs(b - A[idx])
        print(min(l, r))


if __name__ == '__main__':
    solve()
