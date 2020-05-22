# https://atcoder.jp/contests/arc042/submissions/13469367
# B - アリの高橋くん
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    """
    解法概要；
        x,yの座標から板の辺までの最短距離は、x,yから辺への垂線の長さと同じである。
        つまり、x,yから各頂点に線を引いた時にできるn個の三角形の高さの最小値が解となる。

    計算量；O(N)
    :return:
    """
    x, y = map(int, input().split())
    n = int(input())
    XY = [list(map(int, input().split())) for _ in range(n)]

    # 二点間の距離の計算
    def calc_dist(x1, y1, x2, y2):
        return pow(pow(x1 - x2, 2) + pow(y1 - y2, 2), 0.5)

    # 三角形の高さの計算
    def calc_high(x, y, x1, y1, x2, y2):
        a = calc_dist(x, y, x1, y1)
        b = calc_dist(x, y, x2, y2)
        c = calc_dist(x1, y1, x2, y2)
        s = (a + b + c) / 2
        S = pow(s * (s - a) * (s - b) * (s - c), 0.5)
        return (S * 2) / c

    # 三角形の高さの最大値を計算
    res = f_inf
    for i in range(n):
        x1, y1 = XY[i]
        if i == n - 1:
            x2, y2 = XY[0]
        else:
            x2, y2 = XY[i + 1]

        dist = calc_high(x, y, x1, y1, x2, y2)
        res = min(res, dist)

    print(res)


if __name__ == '__main__':
    resolve()
