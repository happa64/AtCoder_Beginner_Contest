# https://atcoder.jp/contests/abc059/submissions/12318271
# B - Comparison
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a = int(input())
    b = int(input())

    if a > b:
        print("GREATER")
    elif a == b:
        print("EQUAL")
    else:
        print("LESS")


if __name__ == '__main__':
    resolve()
