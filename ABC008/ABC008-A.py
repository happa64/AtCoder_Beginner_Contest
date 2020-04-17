# https://atcoder.jp/contests/abc008/tasks/abc008_1
# A - アルバム
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s, t = map(int, input().split())
    print(t - s + 1)


if __name__ == '__main__':
    resolve()
