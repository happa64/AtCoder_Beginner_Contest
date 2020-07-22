# https://atcoder.jp/contests/code-formula-2014-final/submissions/15359941
# F - 100個の円
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    x = y = h = prev = 0
    res = []
    for r in range(1, 101):
        if 1500 < x + 2 * r:
            x = 0
            h += prev
        x += r * 2
        y = h + r
        prev = 2 * r
        res.append((x - r, y))

    for i in res:
        print(*i)


if __name__ == '__main__':
    resolve()
