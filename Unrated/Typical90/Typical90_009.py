# https://atcoder.jp/contests/typical90/submissions/22257062
# 009 - Three Point Angle（★6）
import sys
import math
import cmath

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    XY = [list(map(int, input().split())) for _ in range(n)]

    res = 0
    for i in range(n):
        x1, y1 = XY[i]
        t = []
        for j in range(n):
            if i == j:
                continue
            x2, y2 = XY[j]
            v = complex(x2 - x1, y2 - y1)
            theta = math.degrees(cmath.phase(v))
            t.append(theta)
        t.sort()
        for theta in t:
            idx = bisect_left(t, (theta + 180) % 360)
            s = t[idx - 1] - theta
            res = max(res, min(s, 360 - s))
            if idx != n - 1:
                s = t[idx] - theta
                res = max(res, min(s, 360 - s))
    print(res)


if __name__ == '__main__':
    solve()
