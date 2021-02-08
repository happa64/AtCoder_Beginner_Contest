# https://atcoder.jp/contests/abc191/submissions/19953609
# A - Vanishing Pitch
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    v, t, s, d = map(int, input().split())
    start = v * t
    end = v * s
    if start <= d <= end:
        print("No")
    else:
        print("Yes")


if __name__ == '__main__':
    resolve()
