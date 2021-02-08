# https://atcoder.jp/contests/abc191/submissions/20052470
# D - Circle Lattice Points
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def f(x, y, r, lim):
    res = 0
    left, right = 0, 1
    for i in reversed(range(lim, 10 ** 9 + 10000, 10000)):
        while is_ok(x - left * 10000, i - y, r):
            left -= 1
        while is_ok(right * 10000 - x, i - y, r):
            right += 1
        res += right - left - 1
    return res


def is_ok(dx, dy, r):
    return dx * dx + dy * dy <= r * r


def resolve():
    x, y, r = map(lambda z: round(float(z) * 10000), input().split())
    x %= 10000
    y %= 10000
    res = f(x, y, r, 10000)
    res += f(x, -y, r, 0)
    print(res)


if __name__ == '__main__':
    resolve()
