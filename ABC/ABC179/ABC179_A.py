# https://atcoder.jp/contests/abc179/submissions/16846731
# A - Plural Form
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    if s[-1] == "s":
        print(s + "es")
    else:
        print(s + "s")


if __name__ == '__main__':
    resolve()
