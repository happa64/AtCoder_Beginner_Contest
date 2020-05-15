# https://atcoder.jp/contests/abc070/submissions/13230059
# B - Two Switches
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, c, d = map(int, input().split())
    if a <= c <= d <= b:
        print(d - c)
    elif a <= c <= b <= d:
        print(b - c)
    elif c <= a <= d <= b:
        print(d - a)
    elif c <= a <= b <= d:
        print(b - a)
    else:
        print(0)


if __name__ == '__main__':
    resolve()
