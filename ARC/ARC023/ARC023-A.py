# https://atcoder.jp/contests/arc023/submissions/14512578
# A - 経過日数
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    y = int(input())
    m = int(input())
    d = int(input())

    if m == 1:
        y -= 1
        m = 13
    elif m == 2:
        y -= 1
        m = 14

    init = 365 * 2014 + 2014 // 4 - 2014 // 100 + 2014 // 400 + (306 * (5 + 1)) // 10 + 17 - 429
    delta = 365 * y + y // 4 - y // 100 + y // 400 + (306 * (m + 1)) // 10 + d - 429
    print(abs(delta - init))


if __name__ == '__main__':
    resolve()
