# https://atcoder.jp/contests/abc004/tasks/abc004_4
# D - マーブル 満点解法
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float("inf")
f = lambda a, b: (a + b) * (abs(a - b) + 1) // 2


def calc(Left, Num):
    Right = Left + Num - 1
    if 0 <= Left:
        return f(Right, Left)
    elif Left < 0 < Right:
        return f(0, Right) + f(0, -Left)
    else:
        return f(-Right, -Left)


def resolve():
    R, G, B = map(int, input().split())

    res = f_inf
    for g in range(-300, 300):
        r = min(g - R, -100 - R // 2)
        b = max(g + G, 100 - B // 2)

        res = min(res, calc(r + 100, R) + calc(g, G) + calc(b - 100, B))

    print(int(res))


if __name__ == '__main__':
    resolve()
