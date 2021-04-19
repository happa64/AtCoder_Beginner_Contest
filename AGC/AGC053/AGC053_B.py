# https://atcoder.jp/contests/agc053/submissions/21890636
# B - Taking the middle
import sys
from heapq import *

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    V = list(map(int, input().split()))

    now = []
    aoki = 0
    for i in range(n):
        heappush(now, V[n - (i + 1)])
        heappush(now, V[n + i])
        aoki += heappop(now)

    res = sum(V) - aoki
    print(res)


if __name__ == '__main__':
    solve()
