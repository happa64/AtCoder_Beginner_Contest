# https://atcoder.jp/contests/abc181/submissions/17779989
# A - Heavy Rotation
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    print("White" if n % 2 == 0 else "Black")


if __name__ == '__main__':
    resolve()
