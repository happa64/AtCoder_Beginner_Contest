# https://atcoder.jp/contests/abc197/submissions/21336160
# D - Opposite
import sys
import math

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    """ 複素平面 """
    import cmath

    n = int(input())
    x0, y0 = map(float, input().split())
    xn2, yn2 = map(float, input().split())

    p0 = complex(x0, y0)
    pn2 = complex(xn2, yn2)
    o = (p0 + pn2) / 2
    r = cmath.rect(1, 2 * math.pi / n)
    res = o + (p0 - o) * r
    print(res.real, res.imag)


def solve2():
    """ 回転行列 """
    import numpy as np

    n = int(input())
    p0 = np.array(list(map(float, input().split())))
    pn2 = np.array(list(map(float, input().split())))

    o = (p0 + pn2) / 2
    rad = math.pi * 2 / n
    affine = np.array([[math.cos(rad), -math.sin(rad)], [math.sin(rad), math.cos(rad)]])
    res = affine @ (p0 - o) + o
    print(*res)


def solve3():
    """ 公式想定解法 """

    n = int(input())
    x0, y0 = map(float, input().split())
    xn2, yn2 = map(float, input().split())

    ox, oy = (x0 + xn2) / 2, (y0 + yn2) / 2
    r = pow(pow(xn2 - x0, 2) + pow(yn2 - y0, 2), 0.5) / 2

    theta = math.atan2(y0 - oy, x0 - ox)
    rad = math.pi * 2 / n
    theta += rad

    res = (ox + math.cos(theta) * r, oy + math.sin(theta) * r)
    print(*res)


if __name__ == '__main__':
    solve3()
