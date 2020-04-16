# https://atcoder.jp/contests/abc006/tasks/abc006_3
# C - スフィンクスのなぞなぞ
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())

    # x + y + z = n と 2x + 3y + 4z = m の連立方程式を解くと、z = (m - 2n - y) / 2となる
    # yを全探索すればzが取りうる値が決まる
    y = -1
    z = -1
    for y in range(n):
        t = m - 2 * n - y
        if t >= 0 and t % 2 == 0:
            z = (m - 2 * n - y) // 2
            break

    x = n - y - z
    if x >= 0 and y >= 0 and z >= 0:
        print(x, y, z)
    else:
        print(-1, -1, -1)


if __name__ == '__main__':
    resolve()
