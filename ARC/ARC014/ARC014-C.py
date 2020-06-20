# https://atcoder.jp/contests/arc014/submissions/14488243
# C - 魂の還る場所
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    s = input()

    r = s.count("R") % 2
    g = s.count("G") % 2
    b = s.count("B") % 2
    print(r + g + b)


if __name__ == '__main__':
    resolve()
