# https://atcoder.jp/contests/typical90/submissions/22173098
# 028 - Cluttered Paper（★4）
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    XY = [list(map(int, input().split())) for _ in range(n)]

    MAX = 1000
    imos = [[0] * (MAX + 1) for _ in range(MAX + 1)]

    for lx, ly, rx, ry in XY:
        imos[ly][lx] += 1
        imos[ry][lx] -= 1
        imos[ly][rx] -= 1
        imos[ry][rx] += 1

    for x in range(MAX + 1):
        for y in range(1, MAX + 1):
            imos[y][x] += imos[y - 1][x]

    for y in range(MAX + 1):
        for x in range(1, MAX + 1):
            imos[y][x] += imos[y][x - 1]

    cnt = defaultdict(int)
    for y in range(MAX):
        for x in range(MAX):
            cnt[imos[y][x]] += 1

    for i in range(1, n + 1):
        print(cnt[i])


if __name__ == '__main__':
    solve()