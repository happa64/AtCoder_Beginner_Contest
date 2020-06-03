# https://atcoder.jp/contests/agc002/tasks/agc002_a
# A - Range Product
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b = map(int, input().split())
    if a <= 0 and b >= 0:
        print("Zero")
    elif a > 0:
        print("Positive")
    elif b < 0 and (abs(a - b) + 1) % 2 != 0:
        print("Negative")
    else:
        print("Positive")


if __name__ == '__main__':
    resolve()
