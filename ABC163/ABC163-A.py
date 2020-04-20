# https://atcoder.jp/contests/abc163/tasks/abc163_a
# A - Circle Pond
import sys
import math

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    r = int(input())
    print(2 * r * math.pi)


if __name__ == '__main__':
    resolve()
