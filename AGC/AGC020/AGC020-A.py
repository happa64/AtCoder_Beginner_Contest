# https://atcoder.jp/contests/agc020/submissions/13212667
# A - Move and Win
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, a, b = map(int, input().split())

    if (b - a) % 2 == 0:
        print("Alice")
    else:
        print("Borys")


if __name__ == '__main__':
    resolve()
