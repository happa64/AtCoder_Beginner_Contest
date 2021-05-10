# https://codeforces.com/contest/1487/submission/109065494
# A - Arena
import sys
from bisect import bisect_left

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()

    res = 0
    for i in range(n):
        idx = bisect_left(A, A[i])
        if idx != 0:
            res += 1
    print(res)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()
