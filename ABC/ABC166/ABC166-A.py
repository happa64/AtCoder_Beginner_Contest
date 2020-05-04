# https://atcoder.jp/contests/abc166/tasks/abc166_a
# A - A?C
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    if s == "ABC":
        print("ARC")
    else:
        print("ABC")


if __name__ == '__main__':
    resolve()
