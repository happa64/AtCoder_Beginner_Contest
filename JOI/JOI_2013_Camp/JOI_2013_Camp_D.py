# https://atcoder.jp/contests/joisc2013-day1/submissions/19005721
# 4 - JOIポスター (JOI Poster)
import sys
from itertools import permutations

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7
EPS = 10 ** -8


def resolve():
    n, w, h = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(n)]

    dist = [[0] * n for _ in range(n)]
    for i in range(n):
        x1, y1 = XY[i]
        for j in range(n):
            x2, y2 = XY[j]
            dist[i][j] = pow(pow(x1 - x2, 2) + pow(y1 - y2, 2), 0.5)

    min_dist = [0] * n
    for i in range(n):
        x, y = XY[i]
        min_dist[i] = min(x, w - x, y, h - y)

    res = 0
    for a, b, c, d in permutations(range(n), 4):
        r1 = dist[a][b]
        r2 = dist[c][d]
        dist_ac = dist[a][c]
        if r1 <= min_dist[a] + EPS and r2 <= min_dist[c] + EPS and dist_ac + EPS < abs(r1 - r2):
            res += 1
    print(res // 2)


if __name__ == '__main__':
    resolve()
