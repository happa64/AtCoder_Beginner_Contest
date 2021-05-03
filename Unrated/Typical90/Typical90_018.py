# https://atcoder.jp/contests/typical90/submissions/22249663
# 018 - Statue of Chokudai（★3）
import sys
import math

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def cals_dist(x1, y1, z1, x2, y2, z2):
    return pow(pow(x1 - x2, 2) + pow(y1 - y2, 2) + pow(z1 - z2, 2), 0.5)


def solve():
    T = int(input())
    L, X, Y = map(int, input().split())
    D = L / 2
    q = int(input())
    for _ in range(q):
        e = int(input())
        rad = math.radians(360 * e / T)
        y = -math.sin(rad) * D
        z = D - math.cos(rad) * D
        d = cals_dist(X, Y, 0, 0, y, z)
        theta = math.degrees(math.asin(z / d))
        print(theta)


if __name__ == '__main__':
    solve()
