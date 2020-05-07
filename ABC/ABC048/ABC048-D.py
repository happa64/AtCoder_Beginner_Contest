# https://atcoder.jp/contests/abc048/submissions/12827313
# D - An Ordinary Game
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    n = len(s)

    if (n % 2 == 0) ^ (s[0] == s[-1]):
        print("Second")
    else:
        print("First")


if __name__ == '__main__':
    resolve()
